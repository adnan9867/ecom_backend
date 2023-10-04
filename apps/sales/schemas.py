from datetime import datetime

from pydantic import BaseModel


class SalesListing(BaseModel):
    id = int
    sale_date: datetime
    quantity: int
    total_price: float
    product_id: int


class RevenueSchema(BaseModel):
    date: datetime
    total_revenue: float
