from pydantic import BaseModel
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load environment variables
dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)
first_name = os.environ.get("TEST_FIRST_NAME")
last_name = os.environ.get("TEST_LAST_NAME")

# Define the UserModel
class UserModel(BaseModel):
    first_name: str
    last_name: str
    firebase_uid: str

    # Add an example to the JSON schema
    class Config:
        json_schema_extra = {
            "example": {
                "first_name": first_name,
                "last_name": last_name,
                "firebase_uid": ""
            }
        }