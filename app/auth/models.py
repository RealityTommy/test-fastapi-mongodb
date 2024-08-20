from pydantic import BaseModel
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)
email = os.environ.get("TEST_EMAIL")
password = os.environ.get("TEST_PASSWORD")

class EmailPasswordModel(BaseModel):
    email: str = email
    password: str = password