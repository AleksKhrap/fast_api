from fastapi import FastAPI, HTTPException
from .models import InventoryItem
from .database import add_inventory_item


app = FastAPI()


@app.post("/inventory", response_model=bool)
async def add_inventory_item_api(item: InventoryItem):
    success = add_inventory_item(item)
    if success:
        return True
    else:
        raise HTTPException(status_code=500, detail="Ошибка при добавлении элемента инвентаря")
