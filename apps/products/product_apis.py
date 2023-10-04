from fastapi import APIRouter

from apps.products.product_schemas import ProductListing, ProductCreate
from baselayer.database import SessionLocal
from baselayer.models import Product

product_router = APIRouter()

db = SessionLocal()


@product_router.get("/products", response_model=list[ProductListing])
async def get_products(category_id: int = None):
    products = db.query(Product).all()
    if category_id:
        products = db.query(Product).filter(Product.category_id == category_id).all()
    product_data = [
        {"id": prod.id, "name": prod.name, "description": prod.description, "price": prod.price,
         "category_id": prod.category_id, "category_name": prod.category.name} for prod in products]
    db.close()
    return product_data


@product_router.post("/add-products")
async def add_products(request_data: ProductCreate):
    product = Product(name=request_data.name, description=request_data.description, price=request_data.price,
                      category_id=request_data.category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    db.close()
    return {"message": "Product added successfully"}


@product_router.put("/update-products/{product_id}")
async def update_products(request_data: ProductCreate, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        return {"error": "Product not found"}
    product.name = request_data.name
    product.description = request_data.description
    product.price = request_data.price
    product.category_id = request_data.category_id
    db.commit()
    db.refresh(product)
    db.close()
    return {"message": "Product updated successfully"}
