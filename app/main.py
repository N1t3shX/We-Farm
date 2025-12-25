import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import predict

load_dotenv()

app = FastAPI()

# Development environment CORS configuration - permits all origins
# Note: Restrict origins in production deployment for security
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    """
    Health check endpoint to verify backend service availability.
    """
    return {"message": "Backend is running"}

app.include_router(predict.router)
