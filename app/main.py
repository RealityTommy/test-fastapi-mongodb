from fastapi import FastAPI, Response
from app.auth.auth import router as auth_router
from app.user.user import router as users_router
from app.todo.todo import router as todo_router

app = FastAPI()

# Server Status
@app.get("/")
def root():
    return Response(content="Hello, World", status_code=200)

# Include auth routers
app.include_router(auth_router)

# Include user routers
app.include_router(users_router)

# Include todo routers
app.include_router(todo_router)