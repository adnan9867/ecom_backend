from pydantic import BaseModel


class ProductListing(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int
    category_name: str


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int
