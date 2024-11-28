from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.database import users_collection, token_blacklist
from app.services.auth_service import authenticate_user, create_access_token
from app.models.auth import Token

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
async def logout(token: str):
    token_blacklist.insert_one({"token": token})
    return {"message": "Successfully logged out"}
