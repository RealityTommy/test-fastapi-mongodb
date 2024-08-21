from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import JSONResponse
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from app.config.firebase.config import firebaseConfig
import json
from app.auth.models import EmailPasswordModel
from app.user.models import UserModel
from app.config.mongo.database import db

# Firebase service account key
serviceAccountKeyFile = open("app/config/firebase/serviceAccountKey.json")
serviceAccountKey = json.load(serviceAccountKeyFile)

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(serviceAccountKey)
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)

# MongoDB users collection
user_collection = db["users"]

# Auth router
router = APIRouter(\
    prefix="/auth",\
    tags = ["auth"])

# Sign up with email and password
@router.post("/signup/emailpassword")
async def signup_with_email_and_password(user_login: EmailPasswordModel, user_data: UserModel):
    email = user_login.email
    password = user_login.password

    try:
        user_account = auth.create_user(email=email, password=password)
        
        # If user account is created, create user profile
        if user_account:
            # Sign in user
            signed_in = await signin(user_login)

            # If user is signed in, create user profile
            if signed_in:
                user_profile = UserModel(first_name=user_data.first_name,last_name=user_data.last_name,firebase_uid=user_account.uid)
                user_collection.insert_one(dict(user_profile))

                return Response(content=f"Sign up successful for {email}", status_code=201)

    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail=f"Account already exists for {email}")

# Sign in with email and password
@router.post("/signin/emailpassword")
async def signin(user_login: EmailPasswordModel):
    try:
        user = firebase.auth().sign_in_with_email_and_password(user_login.email, user_login.password)

        token = user["idToken"]

        return JSONResponse(content={"token":token},status_code=200)

    except Exception as e:
        raise HTTPException(detail="Invalid Credentials", status_code=401)

# Validate token
@router.post("/validatetoken")
async def validatetoken(token: str):
    try:
        # Verify the token
        decoded_token = auth.verify_id_token(token)

        return JSONResponse(content={"decoded_token":decoded_token},status_code=200)

    except Exception as e:
        raise HTTPException(detail="Could not validate user", status_code=401)

# Sign out
@router.post("/signout")
async def signout():
    return Response(content="Signout", status_code=200)

# Reset password
@router.post("/resetpassword")
async def resetpassword():
    return Response(content="Reset Password", status_code=200)