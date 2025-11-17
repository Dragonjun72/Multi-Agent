import os
import urllib.parse

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

password = urllib.parse.quote_plus(os.getenv("MYSQL_PASSWORD"))
DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{password}"
    f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DATABASE')}"
)

account_engine = create_engine(DATABASE_URL, echo=True)
AccountSessionLocal = sessionmaker(bind=account_engine)
AccountBase = declarative_base()
