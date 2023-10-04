from fastapi import APIRouter

from apps.products.product_apis import product_router

product = APIRouter()

product.include_router(product_router, tags=["product"])
