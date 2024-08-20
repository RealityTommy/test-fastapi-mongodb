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

serviceAccountKeyFile = open("app/config/firebase/serviceAccountKey.json")
serviceAccountKey = json.load(serviceAccountKeyFile)

if not firebase_admin._apps:
    cred = credentials.Certificate(serviceAccountKey)
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)

collection = db["users"]

router = APIRouter(\
    prefix="/auth",\
    tags = ["auth"])

# Sign up
@router.post("/signup")
async def signup(user_login: EmailPasswordModel, user_data: UserModel):
    email = user_login.email
    password = user_login.password

    try:
        user_account = auth.create_user(email=email, password=password)
        
        if user_account:
            user_profile = UserModel(first_name=user_data.first_name,last_name=user_data.last_name,firebase_uid=user_account.uid)
            collection.insert_one(dict(user_profile))

        return Response(content=f"Sign up successful for user", status_code=201)

    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail=f"Account already exists for {user_login.email}")

# Sign in
@router.post("/signin")
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