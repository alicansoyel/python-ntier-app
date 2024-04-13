from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.conf import settings
import os

db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), settings.SQLITE_DB_NAME))

engine = create_engine(
    f"sqlite:///{db_file}",
    connect_args={"check_same_thread": False},
)
sqlalchemy_url = str(engine.url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base()
def get_db():
    """
    Create a database session.
    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as ex:
        db.rollback()
        raise ex
    finally:
        db.close()