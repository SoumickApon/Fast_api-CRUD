import email
from unicodedata import name
from sqlalchemy import Column, Integer, String
from database import Base

class user(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    email=Column(String(100),unique=True)