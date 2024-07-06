from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Integer, Column, DATETIME


class Base(DeclarativeBase):
    pass


# engine = create_engine('mysql+mysqldb://root:dlwoans@localhost/sample_mysql_db', echo=True)


class UserModel(Base):
    __tablename__ = "users"
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    created_at = Column(DATETIME)
