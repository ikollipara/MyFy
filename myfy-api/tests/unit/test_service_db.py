# unit/test_service_db.py
# Ian Kollipara
# 2021.06.30
# Database Connection Tests

# Imports
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from .. import deps, models

def test_engine():
    assert models.engine is not None
    assert isinstance(models.engine, Engine)

def test_get_db():
    db_gen = deps.get_db()

    assert db_gen is not None
    assert deps.get_db.__doc__ is not None
    for db in db_gen:
        assert isinstance(db, Session)
