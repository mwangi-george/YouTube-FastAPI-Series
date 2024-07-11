from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# a database url --opening a file with the SQLite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app/sql_app.db"

# Database connection engine
engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Database session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for creating database models
Base = declarative_base()
