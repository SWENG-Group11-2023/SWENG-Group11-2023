from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from sqlite import execute_query,create_db
from process import process_query
from constants import *

# creates the db on startup if it does not already exist
create_db()

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


@app.get("/patient/{patient_id}")
async def get_patient(patient_id: str = ""):
    query = f'select * from {DB_TABLE_NAME} where PATIENT="{patient_id}"'
    return execute_query(query)

# use nlp to process query
@app.get("/query/")
async def query_with_nlp(query: str = ""):
    return process_query(query) 