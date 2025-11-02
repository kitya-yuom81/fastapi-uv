from fastapi import FastAPI
from typing import Optional  # same as Union[int, None] but shorter

app = FastAPI()

# GET /
@app.get("/")
def root():
    return {"message": "Hello World"}

# GET /items/{item_id}?page=...&limit=...
@app.get("/items/{item_id}")
def read_item(
    item_id: int,                 # path parameter
    page: Optional[int] = None,   # optional query parameter
    limit: Optional[int] = None,  # optional query parameter
):
    return {
        "item_id": item_id,
        "page": page,
        "limit": limit,
    }

# (optional: run with `python main.py`)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
