from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return{ "item_id": item_id, "q": q}
    