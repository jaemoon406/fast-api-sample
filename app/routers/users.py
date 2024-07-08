from fastapi import APIRouter, FastAPI

from app.models.users import UserModel

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"desc": "Not Found"}}
)


@router.get("/")
async def get_users():
    engine = create_engine(
        "mysql+mysqldb://root:dlwoans@localhost/sample_mysql_db", echo=True
    )
    session = Session(engine)
    with session as session:
        users = session.query(UserModel).all()
    return [
        {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at,
        }
        for user in users
    ]


@router.get("/{user_id}")
async def get_my_data(user_id):
    engine = create_engine(
        "mysql+mysqldb://root:dlwoans@localhost/sample_mysql_db", echo=True
    )
    session = Session(engine)
    with session as session:
        if user := session.query(UserModel).filter(UserModel.id == user_id).first():
            result = {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "created_at": user.created_at,
            }
    return result