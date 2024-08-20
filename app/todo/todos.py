from fastapi import APIRouter, Response
from app.todo.models import Todo
from app.todo.database import collection
from app.todo.schemas import individual_serial, list_serial
from bson import ObjectId

router = APIRouter(\
    prefix='/todos',\
    tags = ['todos'])

# Get all todos
@router.get("/")
async def get_todos():
    try:
        todos = list_serial(collection.find())

        return todos
    
    except Exception as e:
        return {"error": str(e)}

# Create a new todo
@router.post("/")
async def create_todo(name: str, description: str, completed: bool = False):
    todo = Todo(name=name, description=description, completed=completed)

    try:
        collection.insert_one(dict(todo))

        return {"message": "Todo created successfully"}
    
    except Exception as e:
        return {"error": str(e)}

# Update a todo
@router.put("/{id}")
async def update_todo(id: str, name: str, description: str, completed: bool):
    todo = Todo(name=name, description=description, completed=completed)

    try:
        collection.update_one({"_id": ObjectId(id)}, {"$set": dict(todo)})

        return {"message": "Todo updated successfully"}
    
    except Exception as e:
        return {"error": str(e)}

# Delete a todo
@router.delete("/{id}")
async def delete_todo(id: str):
    try:
        collection.delete_one({"_id": ObjectId(id)})

        return {"message": "Todo deleted successfully"}
    
    except Exception as e:
        return {"error": str(e)}

# Get a todo by id
@router.get("/{id}")
async def get_todo(id: str):
    try:
        todo = individual_serial(collection.find_one({"_id": ObjectId(id)}))

        return todo
    
    except Exception as e:
        return {"error": str(e)}

# Delete all todos
@router.delete("/")
async def delete_all_todos():
    try:
        collection.delete_many({})

        return {"message": "All todos deleted successfully"}
    
    except Exception as e:
        return {"error": str(e)}