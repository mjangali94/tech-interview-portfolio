
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import products as product_model
from models import user as user_model


db_url = "postgresql://mj@localhost:5432/postgres"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()