from fastapi import FastAPI
from database import engine,Base,sessionmaker
from models import user


Base.metadata.create_all(bind=engine)

app=FastAPI()

