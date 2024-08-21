from pydantic import BaseModel

# Define the EmailPasswordModel
class EmailPasswordModel(BaseModel):
    email: str
    password: str

    # Add an example to the JSON schema
    class Config:
        json_schema_extra = {
            "example": {
                "email": "test@test.com",
                "password": "password"
            }
        }