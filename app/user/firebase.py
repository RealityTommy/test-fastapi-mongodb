from fastapi import APIRouter, Response
from app.user.models import UserModel as User
from app.user.schemas import individual_serial, list_serial
from bson import ObjectId
from app.auth.auth import validatetoken
from app.auth.firebase import db as firestore

# Firestore users collection
firestore_user_collection = firestore.collection("users")

# Firebase router
router = APIRouter(\
    prefix='/firebase',\
    tags = ['firebase'])

# Get all users
@router.get("/")
async def get_users(token: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, get all users
        if verify_token:
            
            # Get all users
            users = []

            # Iterate through firestore user collection and append to users list
            for doc in firestore_user_collection.stream():
                users.append(doc.to_dict())

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
            # Update the user
            user = firestore_user_collection.document(id).update(dict(user))

            return Response(content="User updated successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Delete a user
@router.delete("/{id}")
async def delete_user(id: str, token: str):
    try:
        # Verify the token
        verify_token = await validatetoken(token)

        # If token is verified, delete the user and all todos
        if verify_token:
            # Delete the user's todos
            firestore_user_collection.document(id).collection("todos").delete()
            # Delete the user
            firestore_user_collection.document(id).delete()

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
            # Get the user
            user = firestore_user_collection.document(id).get()

            # If user exists, return user
            if user:
                return user.to_dict()
    
    except Exception as e:
        return Response(content=str(e), status_code=400)