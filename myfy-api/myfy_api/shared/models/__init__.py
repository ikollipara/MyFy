# models/__init__.py
# Ian Kollipara
# 2021.06.30
# SQLAlchemy Models and Database Intialization

# Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# This is the connection string for the database
SQLALCHEMY_DATABASE_URI = "sqlite:///../../../app.db"

# Initialize the Database Engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

# This is the class that is instaniated in deps.get_db()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
