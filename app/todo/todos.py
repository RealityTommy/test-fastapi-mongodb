from fastapi import APIRouter, Response
from app.todo.models import TodoModel as Todo
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
        return Response(content=str(e), status_code=400)

# Create a new todo
@router.post("/")
async def create_todo(todo: Todo):
    try:
        collection.insert_one(dict(todo))

        return Response(content="Todo created successfully", status_code=201)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Update a todo
@router.put("/{id}")
async def update_todo(todo: Todo, id: str):
    try:
        collection.update_one({"_id": ObjectId(id)}, {"$set": dict(todo)})

        return Response(content="Todo updated successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete a todo
@router.delete("/{id}")
async def delete_todo(id: str):
    try:
        collection.delete_one({"_id": ObjectId(id)})

        return Response(content="Todo deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Get a todo by id
@router.get("/{id}")
async def get_todo(id: str):
    try:
        todo = individual_serial(collection.find_one({"_id": ObjectId(id)}))

        return todo
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete all todos
@router.delete("/")
async def delete_all_todos():
    try:
        collection.delete_many({})

        return Response(content="All todos deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)