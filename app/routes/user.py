from fastapi import APIRouter, HTTPException, Depends
from app.models.user import UserCreate, UserResponse
from app.services.auth_service import get_current_user, has_role
from app.services.user_service import create_user, get_users

router = APIRouter()

@router.post("/", response_model=UserResponse, dependencies=[Depends(has_role("admin"))])
async def create_new_user(user: UserCreate):
    return create_user(user)

@router.get("/", response_model=list[UserResponse], dependencies=[Depends(get_current_user)])
async def list_users():
    return get_users()
