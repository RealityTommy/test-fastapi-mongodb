from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
import os
from os.path import join, dirname
from dotenv import load_dotenv

app = FastAPI()

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)
username = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
password = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
uri=f"mongodb://{username}:{password}@mongo:27017/?authSource=admin"

client = MongoClient(uri)

db = client.todo

collection = db["todos"]