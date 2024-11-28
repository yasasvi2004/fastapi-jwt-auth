from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    hashed_password: str
    role: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    role: Optional[str] = "user"

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    full_name: str
    role: str
