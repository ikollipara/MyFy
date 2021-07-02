# deps/db.py
# Ian Kollipara
# 2021.06.30
# Database Access Dependency

# Imports
from sqlalchemy.orm import Session
from ..models import SessionLocal

def get_db() -> Session:
    """ Get the Database Session.

    This function is designed after
    the specification given on the
    FastAPI docs for a functional
    dependency. It uses the example
    behavior.

    returns: sqlalchemy.orm.Session
    """

    db: Session = SessionLocal()

    try:
        yield db

    finally:
        db.close()
