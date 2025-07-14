from fastapi import FastAPI
from app.routers import badges, certificates

app = FastAPI(
    title="Badge & Certificate Issuer API",
    version="1.0.0"
)

# Include routers
app.include_router(badges.router)
app.include_router(certificates.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Badge & Certificate Issuer API"}
