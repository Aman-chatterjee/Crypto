import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
PORT = os.getenv('PORT')
DB_NAME = os.getenv('DB_NAME')
DATABASE_URL = f'postgresql://postgres:{DB_PASSWORD}@localhost:{PORT}/{DB_NAME}'

#Setting up postgres sql
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()