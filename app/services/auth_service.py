from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from app.database import users_collection, token_blacklist
from app.config import JWT_SECRET_KEY, JWT_ALGORITHM
from fastapi.security import OAuth2PasswordBearer


def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=30)})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

def authenticate_user(username: str, password: str):
    user = users_collection.find_one({"username": username})
    if user and user["hashed_password"] == password:  # Replace with proper hashing
        return user
    return None

def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        username = payload.get("sub")
        user = users_collection.find_one({"username": username})
        if user is None or token_blacklist.find_one({"token": token}):
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def has_role(required_role: str):
    def role_checker(current_user=Depends(get_current_user)):
        if current_user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Access denied")
    return role_checker
