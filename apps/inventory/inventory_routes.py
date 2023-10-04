from fastapi import APIRouter

from apps.inventory.inventory_management import inventory_router

inventory = APIRouter()

inventory.include_router(inventory_router, tags=["inventory"])
