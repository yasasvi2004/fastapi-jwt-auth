from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["fastapi_auth"]  # Database name
users_collection = db["users"]  # Collection for users
token_blacklist = db["blacklisted_tokens"]  # Collection for blacklisted tokens
