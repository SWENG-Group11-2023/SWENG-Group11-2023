from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from sqlite import execute_query,create_db
from process import process_query,descriptions_to_json, download_to_csv
from constants import *
import nltk

# checks if nltk packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# creates the db on startup if it does not already exist
create_db()
# creates description.json if does not exist
descriptions_to_json()

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
@app.get("/query/{query}")
async def query_with_nlp(query: str = ""):
    return process_query(query)

# use nlp to to create downloadable csv format
@app.get("/download/{query}")
async def download(query: str = ""):
    return download_to_csv(query) 