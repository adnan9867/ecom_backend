from pydantic import BaseModel


class InventoryCreate(BaseModel):
    product_id: int
    quantity: int


class InventoryResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    low_stock: bool


class InventoryUpdate(BaseModel):
    quantity: int
