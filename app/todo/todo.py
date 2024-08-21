from fastapi import APIRouter
from app.todo.mongo import router as todos_mongo_router
from app.todo.firebase import router as todos_firebase_router

router = APIRouter(\
    prefix='/todos',\
    tags = ['todos'])

router.include_router(todos_mongo_router)

router.include_router(todos_firebase_router)