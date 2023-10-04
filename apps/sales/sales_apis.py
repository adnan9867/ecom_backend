from typing import Union

from sqlalchemy import text

from fastapi import APIRouter, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Query

from apps.sales.schemas import SalesListing, RevenueSchema
from baselayer.database import SessionLocal
from baselayer.models import Sale, Product

sales = APIRouter()
db = SessionLocal()


@sales.get("/get_sales/{sale_id}")
async def read_sale(sale_id: int):
    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    db.close()
    if sale is None:
        return {"error": "Sale not found"}
    return sale


@sales.get("/revenue",  response_model=list[RevenueSchema])
async def get_revenue(
        period: str,
        category_id: int = None,
        start_date: str = None,
        end_date: str = None
):
    if period not in ["day", "week", "month"]:
        raise HTTPException(status_code=400, detail="Invalid period. Allowed values are 'day,' 'week,' and 'month.'")

        # Build the query for revenue calculation
    query = db.query(
        func.date_trunc(period, Sale.sale_date).label("period"),
        func.sum(Sale.total_price).label("total_revenue")
    )

    # Add optional filters for category and custom date range
    if category_id:
        query = query.join(Product).filter(Product.category_id == category_id)

    if start_date and end_date:
        query = query.filter(Sale.sale_date.between(start_date, end_date))

    # Group and order the results

    # Group and order the results
    query = query.group_by("period").order_by("period")

    # Execute the query and get the results
    revenue_data = query.all()

    # Close the database session
    db.close()

    # Check if any revenue data was found
    if not revenue_data:
        raise HTTPException(status_code=404, detail="No revenue data found")

    # Format the response as a list of dictionaries
    formatted_data = [{"date": row[0], "total_revenue": row[1]} for row in revenue_data]

    return formatted_data


@sales.get("/sales_listing")
async def compare_revenue(
        start_date: str,
        end_date: str,
        category_id: int = None,
        product_id: int = None
):
    query = db.query(Sale).filter(Sale.sale_date >= start_date, Sale.sale_date <= end_date)
    if category_id:
        query = query.join(Product).filter(Product.category_id == category_id)

    if product_id:
        query = query.filter(Sale.product_id == product_id)

    revenue_data = query.all()
    db.close()
    return revenue_data
