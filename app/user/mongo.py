from fastapi import APIRouter, Response
from app.user.models import UserModel as User
from app.user.schemas import individual_serial, list_serial
from bson import ObjectId
from app.config.mongo.database import db

collection = db["users"]

router = APIRouter(\
    prefix='/mongo',\
    tags = ['mongo'])

# Get all users
@router.get("/")
async def get_users():
    try:
        users = list_serial(collection.find())

        return users
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Create a new user
@router.post("/")
async def create_user(user: User):
    try:
        collection.insert_one(dict(user))

        return Response(content="User created successfully", status_code=201)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Update a user
@router.put("/{id}")
async def update_user(user: User, id: str):
    try:
        collection.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})

        return Response(content="User updated successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete a user
@router.delete("/{id}")
async def delete_user(id: str):
    try:
        collection.delete_one({"_id": ObjectId(id)})

        return Response(content="User deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Get a user by id
@router.get("/{id}")
async def get_user(id: str):
    try:
        user = individual_serial(collection.find_one({"_id": ObjectId(id)}))

        return user
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete all users
@router.delete("/")
async def delete_all_users():
    try:
        collection.delete_many({})

        return Response(content="All users deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)