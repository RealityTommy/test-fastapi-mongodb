from fastapi import FastAPI
import os
from pymongo.mongo_client import MongoClient

app = FastAPI()

username = os.environ.get('MONGO_INITDB_ROOT_USERNAME', '')
password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', '')
uri=f"mongodb://root:password@mongo:27017/?authSource=admin"
client = MongoClient(uri)

db = client.todo

collection = db["todos"]