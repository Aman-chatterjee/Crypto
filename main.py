from routes import auth, crypto
from fastapi import FastAPI
from models.base import Base
from database import engine


# fastapi run main.py

app = FastAPI()
app.include_router(auth.router, prefix="/auth")
app.include_router(crypto.router)
Base.metadata.create_all(engine)

