from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from SQLiteExample import ExecuteQuery

# config stuff to expose to frontend application
middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middlewares)

# returns hello world on the root
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "description": f"{item_id} is an item"}

# returns all rows with given patient ID using SQLiteExample.py
@app.get("/patient/{patient_id}")
async def run_query(patient_id: str):
    query = f'select * from test where PATIENT="{patient_id}"'
    return ExecuteQuery(query=query)
