from pydantic import BaseModel

app = FastAPI()

# הגדרת מודל ל-request body
class Item(BaseModel):
    name: str
    price: float
    description: str = None  # שדה אופציונלי

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_description": item.description}