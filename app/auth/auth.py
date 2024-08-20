from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
import requests
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from app.config.firebase.config import firebaseConfig
import json
from app.auth.models import EmailPasswordModel

serviceAccountKeyFile = open("app/config/firebase/serviceAccountKey.json")
serviceAccountKey = json.load(serviceAccountKeyFile)

if not firebase_admin._apps:
    cred = credentials.Certificate(serviceAccountKey)
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)

router = APIRouter(\
    prefix="/auth",\
    tags = ["auth"])

# Sign up
@router.post("/signup")
async def signup(user_data: EmailPasswordModel):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.create_user(email=email, password=password)
        
        return Response(content=f"Sign up successful for user {user.uid}", status_code=201)

    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail=f"Account already exists for {email}")

# Sign in
@router.post("/signin")
async def signin(user_data: EmailPasswordModel):
    email = user_data.email
    password = user_data.password

    try:
        user = firebase.auth().sign_in_with_email_and_password(email, password)

        token = user["idToken"]

        return JSONResponse(content={"token":token},status_code=200)

    except Exception as e:
        raise HTTPException(detail="Invalid Credentials", status_code=400)

# Sign out
@router.post("/signout")
async def signout():
    return Response(content="Signout", status_code=200)

# Reset password
@router.post("/resetpassword")
async def resetpassword():
    return Response(content="Reset Password", status_code=200)