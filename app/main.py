from fastapi import FastAPI, Response
from app.todo.todos import router as todos_router

app = FastAPI()

# Server Status
@app.get("/")
def root():
    return Response(content="Server is running", status_code=200)

app.include_router(todos_router)