from fastapi import FastAPI, Response
from app.auth.auth import router as auth_router
from app.todo.todos import router as todos_router

app = FastAPI()

# Server Status
@app.get("/")
def root():
    return Response(content="Hello, World", status_code=200)

app.include_router(auth_router)

app.include_router(todos_router)