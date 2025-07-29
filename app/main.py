from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers import badges, certificates
from app.database import connect_to_mongo, close_mongo_connection
from app.auth.auth_handler import get_api_key

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()

app = FastAPI(
    title="Badge & Certificate Issuer API",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
origins = [
    "https://localhost",
    "https://localhost:5173",  # React default port
    "https://localhost:8000",  # FastAPI default port
    "https://zcertify.zairza.co.in",  # Your production domain
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(badges.router)
app.include_router(certificates.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Badge & Certificate Issuer API"}
