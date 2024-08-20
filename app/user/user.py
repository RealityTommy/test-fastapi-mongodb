from fastapi import APIRouter
from app.user.mongo import router as users_mongo_router

router = APIRouter(\
    prefix='/users',\
    tags = ['users'])

router.include_router(users_mongo_router)