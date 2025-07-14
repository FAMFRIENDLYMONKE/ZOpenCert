from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import badges, certificates
from app.database import connect_to_mongo, close_mongo_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_to_mongo()
    yield
    close_mongo_connection()

app = FastAPI(
    title="Badge & Certificate Issuer API",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(badges.router)
app.include_router(certificates.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Badge & Certificate Issuer API"}