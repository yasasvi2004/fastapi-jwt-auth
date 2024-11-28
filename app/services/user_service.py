from app.database import users_collection
from app.models.user import UserCreate, UserResponse

def create_user(user: UserCreate):
    new_user = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": user.password,  # Replace with proper hashing
        "role": user.role
    }
    result = users_collection.insert_one(new_user)
    return UserResponse(id=str(result.inserted_id), **new_user)

def get_users():
    return [UserResponse(id=str(user["_id"]), **user) for user in users_collection.find()]
