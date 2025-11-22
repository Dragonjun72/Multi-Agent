from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from config.database.session import Base


class NewsORM(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(512), nullable=False)
    description = Column(Text, nullable=True)
    originallink = Column(String(1024), nullable=True)
    link = Column(String(1024), nullable=False, unique=True, index=True)
    pub_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)