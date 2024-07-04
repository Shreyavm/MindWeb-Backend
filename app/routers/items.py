from fastapi import APIRouter
from models.item import Item


router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@router.post("/items/")
def create_item(item: Item):
    return {"item_id": item.id, "name": item.name, "description": item.description}
