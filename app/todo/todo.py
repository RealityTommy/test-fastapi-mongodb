from fastapi import APIRouter
from app.todo.mongo import router as todos_mongo_router

router = APIRouter(\
    prefix='/todos',\
    tags = ['todos'])

router.include_router(todos_mongo_router)