from fastapi import APIRouter, Response
from app.todo.models import TodoModel as Todo
from app.todo.schemas import individual_serial, list_serial
from bson import ObjectId
from app.config.mongo.database import db
from app.auth.auth import validatetoken

# MongoDB todo collection
todo_collection = db["todos"]

# Todo router
router = APIRouter(\
    prefix='/mongo',\
    tags = ['mongo'])

# Get all todos
@router.get("/")
async def get_todos(token: str, firebase_uid: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, get all todos
        if verify_token:
            todos = list_serial(todo_collection.find({"firebase_uid": firebase_uid}))

            return todos
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Create a new todo
@router.post("/")
async def create_todo(token: str, todo: Todo, firebase_uid: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, create the todo
        if verify_token:
            # Create the todo
            new_todo = Todo(\
                name = todo.name,\
                description = todo.description,\
                completed = todo.completed,\
                firebase_uid = firebase_uid\
            )

            # Insert the todo into the todo collection
            todo_collection.insert_one(dict(new_todo))

            return Response(content="Todo created successfully", status_code=201)

    except Exception as e:
        return Response(content=str(e), status_code=400)

# Update a todo
@router.put("/{id}")
async def update_todo(token: str, todo: Todo, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, update the todo
        if verify_token:
            todo_collection.update_one({"_id": ObjectId(id)}, {"$set": dict(todo)})

            return Response(content="Todo updated successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete a todo
@router.delete("/{id}")
async def delete_todo(token: str, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, delete the todo
        if verify_token:
            todo_collection.delete_one({"_id": ObjectId(id)})

            return Response(content="Todo deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Get a todo by id
@router.get("/{id}")
async def get_todo(token: str, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, get the todo
        if verify_token:
            todo = individual_serial(todo_collection.find_one({"_id": ObjectId(id)}))

            return todo
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete all todos for a user
@router.delete("/")
async def delete_all_todos(token: str, firebase_uid: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, delete all todos for the user
        if verify_token:
            todo_collection.delete_many({"firebase_uid": firebase_uid})

            return Response(content="All todos deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)