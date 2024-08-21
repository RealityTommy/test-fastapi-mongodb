from fastapi import APIRouter, Response
from app.user.models import UserModel as User
from app.user.schemas import individual_serial, list_serial
from bson import ObjectId
from app.config.mongo.database import db
from app.auth.auth import validatetoken

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

# Create a new user
@router.post("/")
async def create_user(user: User):
    try:
        user_collection.insert_one(dict(user))

        return Response(content="User created successfully", status_code=201)
    
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
async def delete_user(uid: str, token: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, delete the user and all todos
        if verify_token:
            user = list_serial(user_collection.find({"firebase_uid": uid}))

            if user:
                # Delete all the user's todos
                todo_collection.delete_many({"uid": uid})

                # Delete the user
                user_collection.delete_one({"firebase_uid": uid})

                return Response(content="User deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Get a user by id
@router.get("/{id}")
async def get_user(token: str, id: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, get the user
        if verify_token:
            user = individual_serial(user_collection.find_one({"_id": ObjectId(id)}))

            return user
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete all users
@router.delete("/")
async def delete_all_users(token: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, delete all users
        if verify_token:
            # Delete all users
            user_collection.delete_many({})

            return Response(content="All users deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)