from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from account.infrastructure.config.mysql_config import AccountBase


class ProfileORM(AccountBase):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    bio = Column(String(1024), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
