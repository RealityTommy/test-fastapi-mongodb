from fastapi import FastAPI, Response
from app.todo.todos import router as todos_router

app = FastAPI()

app.include_router(todos_router)

# Server Status
@app.get("/")
def root():
    return Response("Server is running.")

app.include_router(todos_router)