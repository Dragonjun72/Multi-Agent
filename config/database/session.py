from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session, sessionmaker, declarative_base
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

password = urllib.parse.quote_plus(os.getenv("MYSQL_PASSWORD"))

DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{password}"
    f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DATABASE')}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#def get_db_session():

def get_db_session() -> Session:
    """Return a new SQLAlchemy session."""
    return SessionLocal()


def get_db_session_dependency():
    """FastAPI dependency that yields a session and ensures closure."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()