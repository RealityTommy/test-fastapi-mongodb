from fastapi import APIRouter, Response
from app.todo.models import TodoModel as Todo
from app.todo.schemas import individual_serial, list_serial
from bson import ObjectId
from app.auth.auth import validatetoken
from app.auth.firebase import db as firestore

# Firestore users collection
firestore_user_collection = firestore.collection("users")

# Todo router
router = APIRouter(\
    prefix='/firebase',\
    tags = ['firebase'])

# Get all todos
@router.get("/")
async def get_todos(token: str, firebase_uid: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, create the todo
        if verify_token:
            # Get all todos
            todos = []

            # Iterate through firestore user's todos collection and append to todos list
            for doc in firestore_user_collection.document(firebase_uid).collection("todos").stream():
                todos.append(doc.to_dict())

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
            new_todo = Todo(name=todo.name, description=todo.description, completed=todo.completed, firebase_uid=firebase_uid)

            # Get the user's todos collection
            user_todos = firestore_user_collection.document(firebase_uid).collection("todos")

            # Insert the todo into the user's todos collection
            user_todos.document().set(dict(new_todo))

            return Response(content="Todo created successfully", status_code=201)

    except Exception as e:
        return Response(content=str(e), status_code=400)

# Update a todo
@router.put("/{id}")
async def update_todo(token: str, todo: Todo, firebase_uid: str, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, update the todo
        if verify_token:
            # Update the user
            update_todo = firestore_user_collection.document(firebase_uid).collection("todos").document(id).update(dict(todo))

            return Response(content="Todo updated successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete a todo
@router.delete("/{id}")
async def delete_todo(token: str, firebase_uid:str, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, delete the todo
        if verify_token:
            # Delete the todo
            firestore_user_collection.document(firebase_uid).collection("todos").document(id).delete()

            return Response(content="Todo deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Get a todo by id
@router.get("/{id}")
async def get_todo(token: str, firebase_uid: str, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, get the todo
        if verify_token:
            # Get the todo
            todo = firestore_user_collection.document(firebase_uid).collection("todos").document(id).get()

            # If todo exists, return todo
            if todo:
                return todo.to_dict()

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
            # Iterate through firestore user's todos collection and delete each todo
            for doc in firestore_user_collection.document(firebase_uid).collection("todos").stream():
                delete_todos = await delete_todo(token, firebase_uid, doc.id)

            return Response(content="All todos deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)