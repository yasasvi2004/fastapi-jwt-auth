from fastapi import FastAPI
from app.routes import auth, user
from app.utils.logger import setup_logging

app = FastAPI(title="FastAPI JWT Auth System", version="1.0")

# Setup logging
setup_logging()

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/users", tags=["User Management"])
