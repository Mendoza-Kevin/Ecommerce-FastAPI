from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgres://:postgres:123456@localhost:5432/ecommerce_db"

engine = create_engine(DATABASE_URL)
SessionmLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)