from pydantic import BaseModel
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load environment variables
dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)
email = os.environ.get("TEST_EMAIL")
password = os.environ.get("TEST_PASSWORD")

# Define the EmailPasswordModel
class EmailPasswordModel(BaseModel):
    email: str = email
    password: str = password

    # Add an example to the JSON schema
    class Config:
        json_schema_extra = {
            "example": {
                "email": email,
                "password": password
            }
        }