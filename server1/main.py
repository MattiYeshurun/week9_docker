import json
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

DB_PATH = Path("db/shopping_list.json")

@app.get("/items")
def load_database():
    with open(DB_PATH, "r") as f:
            return json.load(f)

class Item(BaseModel):
    id: int
    name: str
    quantity: int

@app.post("/items/")
async def create_item(item: Item):
    return item



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)