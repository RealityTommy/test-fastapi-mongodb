from pydantic import BaseModel

class Todo(BaseModel):
    name: str = "Name"
    description: str = "Description"
    completed: bool = False