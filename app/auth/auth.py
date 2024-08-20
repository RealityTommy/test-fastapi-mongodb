from fastapi import APIRouter, Response
import pyrebase
import firebase_admin
from firebase_admin import credentials
from config.firebase.config import firebase_config

if not firebase_admin._apps:
    cred = credentials.Certificate("../../config/firebase/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebase_config)

router = APIRouter(\
    prefix='/auth',\
    tags = ['auth'])

# Sign up
@router.post("/signup")
async def signup():
    return Response(content="Signup", status_code=200)

# Sign in
@router.post("/signin")
async def signin():
    return Response(content="Signin", status_code=200)

# Validate token
@router.post("/validate")
async def validate():
    return Response(content="Validate", status_code=200)

# Sign out
@router.post("/signout")
async def signout():
    return Response(content="Signout", status_code=200)