from fastapi import FastAPI, APIRouter
from app.routers.users import router
import uvicorn
from .routers import users

app = FastAPI()


# @router.get('/')
# async def root():
#     return {"message": "Hello sample web server"}


# app.include_router(router)
app.include_router(router)
