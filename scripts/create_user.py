import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
users_collection = client["fastapi_auth"]["users"]

users_collection.insert_one({
    "username": "admin",
    "email": "admin@example.com",
    "full_name": "Admin User",
    "hashed_password": "admin123",  # Replace with hashed password
    "role": "admin"
})

print("Admin user created.")
