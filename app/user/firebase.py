from fastapi import APIRouter, Response
from app.user.models import UserModel as User
from app.user.schemas import individual_serial, list_serial
from bson import ObjectId
from app.auth.auth import validatetoken

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
            # TODO: Get all users from Firebase
            users = list_serial()

            return users
    
    except Exception as e:
        return Response(content=str(e), status_code=400)

# Create a new user
@router.post("/")
async def create_user(user: User):
    try:

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
            # TODO: Update the user in Firebase

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
            # TODO: Get the user from Firebase
            user = list_serial()

            if user:
                # Delete all the user's todos
                # TODO: Delete the user's todos from Firebase

                # Delete the user
                # TODO: Delete the user from Firebase

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
            # TODO: Get the user from Firebase

            return Response(content="User", status_code=200)
    
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
            # TODO: Delete all users from Firebase

            return Response(content="All users deleted successfully", status_code=200)
    
    except Exception as e:
        return Response(content=str(e), status_code=400)