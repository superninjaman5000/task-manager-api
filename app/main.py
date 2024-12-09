from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await init_db()
    yield  # Keeps the app running
    # Shutdown logic (if needed)
    # Add cleanup tasks here if required

# Initialize FastAPI app with the lifespan handler
app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}
