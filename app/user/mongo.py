from fastapi import APIRouter, Response
from app.user.models import UserModel as User
from app.user.schemas import individual_serial, list_serial
from bson import ObjectId
from app.config.mongo.database import db
from app.auth.auth import validatetoken
from app.todo.mongo import delete_all_todos

user_collection = db["users"]
todo_collection = db["todos"]

router = APIRouter(\
    prefix='/mongo',\
    tags = ['mongo'])

# Get all users
@router.get("/")
async def get_users(token: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, get all users
        if verify_token:
            users = list_serial(user_collection.find())

            return users
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Update a user
@router.put("/{id}")
async def update_user(token: str, user: User, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, update the user
        if verify_token:
            user_collection.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})

            return Response(content="User updated successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete a user
@router.delete("/{id}")
async def delete_user(token: str, firebase_uid: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, delete the user and all todos
        if verify_token:
            user = list_serial(user_collection.find({"firebase_uid": firebase_uid}))

            if user:
                # Delete all the user's todos
                todo_collection.delete_many({"firebase_uid": firebase_uid})

                # Delete the user
                user_collection.delete_one({"firebase_uid": firebase_uid})

                return Response(content="User deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Get a user by id
@router.get("/{id}")
async def get_user(token: str, firebase_uid: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, get the user
        if verify_token:
            delete_todos = await delete_all_todos(token, firebase_uid)

            user = individual_serial(user_collection.find_one({"firebase_uid": firebase_uid}))

            return user
    
    except Exception as e:
        return Response(content=str(e), status_code=400)