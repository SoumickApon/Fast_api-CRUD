import email
from unicodedata import name
from pydantic import BaseModel


class Record(BaseModel):
    id: int
    name:str
    email:str

    class Config:
        orm_mode = True