from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = None

items_db: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API!"}

@app.get("/Items")
def define_items():
    return items_db

@app.post("/Item_list")
def list_item(item: Item):
    items_db.append(item)
    return {"message": "Item added successfully", "item": item}

@app.put("/Item_update/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return {"message": "Item updated successfully", "item": updated_item}
    return {"error": "Item not found"}


@app.delete("/Item_delete/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(index)
            return {"message": "Item deleted successfully", "item": deleted_item}
    return {"error": "Item not found"}