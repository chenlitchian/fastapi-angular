# starter
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

# GET path
@app.get('/path_name')
def method_name():
    pass


# async
@app.get('/path_name')
async def method_name():
    pass

@app.post('/path_name')
def method_name():
    pass

@app.post('/path_name')
async def method_name():
    pass

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'db_url'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

@app.on_event('startup')
async def on_startup():
    pass

@app.on_event('shutdown')
async def on_shutdown():
    pass











