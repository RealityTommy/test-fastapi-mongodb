from pydantic import BaseModel
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)
first_name = os.environ.get("TEST_FIRST_NAME")
last_name = os.environ.get("TEST_LAST_NAME")

class UserModel(BaseModel):
    first_name: str = first_name
    last_name: str = last_name
    firebase_uid: str = None