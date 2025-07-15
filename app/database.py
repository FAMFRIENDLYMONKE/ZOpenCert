from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = None
db = None
badge_collection = None
certificate_collection = None

async def connect_to_mongo():
    global client, db, badge_collection, certificate_collection

    client = AsyncIOMotorClient(MONGO_URL)
    db = client["certificate_platform"]
    print("Connected to MongoDB")
    badge_collection = db["badges"]
    certificate_collection = db["certificates"]


async def close_mongo_connection():
    global client
    if client:
        client.close()
 
def get_badge_collection():
    global badge_collection
    if badge_collection is None:
        raise Exception("Database not connected yet. Call connect_to_mongo() first.")
    return badge_collection

def get_certificate_collection():
    global certificate_collection
    if certificate_collection is None:
        raise Exception("Database not connected yet. Call connect_to_mongo() first.")
    return certificate_collection