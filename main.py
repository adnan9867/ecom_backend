from fastapi import FastAPI
from apps.inventory.inventory_routes import inventory
from apps.products.routers import product
from apps.sales.sales_routes import sale_router
from upload_dump import create_dummy_categories, create_dummy_products, create_dummy_sales, create_dummy_inventory

app = FastAPI()

app.include_router(router=sale_router, prefix="/api/v1")
app.include_router(router=inventory)
app.include_router(router=product)


