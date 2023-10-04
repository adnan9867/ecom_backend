from fastapi import APIRouter, HTTPException

from apps.inventory.schemas import InventoryResponse, InventoryUpdate
from baselayer.database import SessionLocal
from baselayer.models import Inventory

sales = APIRouter()

inventory_router = APIRouter()

db = SessionLocal()


@inventory_router.get("/inventory", response_model=list[InventoryResponse])
async def get_inventory(product_id: int = None):
    inventories = db.query(Inventory).all()
    if product_id:
        inventories = db.query(Inventory).filter(Inventory.product_id == product_id).all()
    db.close()
    inventory_data = [
        {"id": inv.id, "product_id": inv.product_id, "quantity": inv.quantity, "low_stock": inv.quantity < 20} for inv
        in inventories]
    return inventory_data


@inventory_router.put("/inventory/{inventory_id}")
async def update_inventory(request_data: InventoryUpdate, inventory_id: int):
    inventory = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventory.quantity = request_data.quantity
    db.commit()
    db.refresh(inventory)
    db.close()
    return {"message": "Inventory updated successfully"}
