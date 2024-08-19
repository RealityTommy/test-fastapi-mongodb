from fastapi import APIRouter, Response
from app.todo.models import Todo
from app.todo.database import collection
from app.todo.schemas import individual_serial, list_serial
from bson import ObjectId

router = APIRouter(\
    prefix='/todos',\
    tags = ['todos'])

# GET Request Method
@router.get("/")
async def get_todos():
    try:
        todos = list_serial(collection.find())

        return todos
    
    except Exception as e:
        return {"error": str(e)}

# POST Request Method
@router.post("/")
async def create_todo(name: str, description: str, completed: bool = False):
    todo = Todo(name=name, description=description, completed=completed)

    try:
        collection.insert_one(dict(todo))

        return {"message": "Todo created successfully"}
    
    except Exception as e:
        return {"error": str(e)}

# PUT Request Method
@router.put("/{id}")
async def update_todo(id: str, name: str, description: str, completed: bool):
    todo = Todo(name=name, description=description, completed=completed)

    try:
        collection.update_one({"_id": ObjectId(id)}, {"$set": dict(todo)})

        return {"message": "Todo updated successfully"}
    
    except Exception as e:
        return {"error": str(e)}

# DELETE Request Method
@router.delete("/{id}")
async def delete_todo(id: str):
    try:
        collection.delete_one({"_id": ObjectId(id)})

        return {"message": "Todo deleted successfully"}
    
    except Exception as e:
        return {"error": str(e)}

# GET Request Method
@router.get("/{id}")
async def get_todo(id: str):
    try:
        todo = individual_serial(collection.find_one({"_id": ObjectId(id)}))

        return todo
    
    except Exception as e:
        return {"error": str(e)}

# DELETE Request Method
@router.delete("/")
async def delete_all_todos():
    try:
        collection.delete_many({})

        return {"message": "All todos deleted successfully"}
    
    except Exception as e:
        return {"error": str(e)}