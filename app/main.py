import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager # decorator import
from fastapi.staticfiles import StaticFiles

from app.config import settings

from app.routers.base_router import base_router

# Use the asynccontextmanager decorator for lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print("Server is down :(")

# Create an instance of APP(FastAPI)
app = FastAPI(lifespan=lifespan)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect the router
app.include_router(base_router)

# For static files to work
app.mount("/static", StaticFiles(directory="static"), name="static")

# Server startup with automatic restart
if __name__ == "__main__":
    uvicorn.run("app.main:app",  reload=settings.reload, host=settings.host, port=settings.port)
