from fastapi import APIRouter

from apps.sales.sales_apis import sales

sale_router = APIRouter()

sale_router.include_router(sales, tags=["sales"])
