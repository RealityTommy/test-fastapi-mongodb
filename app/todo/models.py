from pydantic import BaseModel

class TodoModel(BaseModel):
    name: str = "Name"
    description: str = "Description"
    completed: bool = False