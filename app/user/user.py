from fastapi import APIRouter
from app.user.mongo import router as users_mongo_router
from app.user.firebase import router as users_firebase_router

router = APIRouter(\
    prefix='/users',\
    tags = ['users'])

router.include_router(users_mongo_router)

router.include_router(users_firebase_router)