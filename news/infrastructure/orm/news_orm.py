from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text, String

from config.database.session import Base


class NewsORM(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
