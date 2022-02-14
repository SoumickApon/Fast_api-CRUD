from fastapi import Depends, FastAPI, HTTPException
from database import engine,Base,SessionLocal
from models import user
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserSchema(BaseModel):
    name:str
    email:str
    class Config:
        orm_model=True

class UserCreate(BaseModel):
    password:str

@app.get("/user",response_model=List[UserSchema])
def get_users(db:Session=Depends(get_db)):
    return db.query(user).all()

@app.post("/user",response_model=UserSchema)
def post_user(user:UserCreate,db:Session=Depends(get_db)):
    u = Users(name=user.name,email=user.email,password=user.password)
    db.add(u)
    db.commit()
    return u
@app.put("/user/{user_id}",response_model=UserSchema)
def update_user(user_id:int,user:UserSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id==user_id).filter()
        u.name=user.name
        u.email=user.email
        db.add(u)
        db.commit()
        return u 
    except:
        return HTTPException(status_code=404,detail="user not found")

@app.delete("/user/{user_id}",response_class=JSONResponse)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id==user_id).filter()
        db.delete(u)
        return {f"user of id {user_id} has been delete":True}
    except:
        return HTTPException(status_code=404,detail="user not found")