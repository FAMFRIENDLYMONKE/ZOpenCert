from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = None
db = None

def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGO_URL)
    db = client["certificate_platform"]
    print("Connected to MongoDB.")

def close_mongo_connection():
    global client
    if client:
        client.close()
        print("Disconnected from MongoDB.")

# Collections
badge_collection = db["badges"]
certificate_collection = db["certificates"]