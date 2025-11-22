from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from config.database.session import Base


class NewsModel(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(512))
    description = Column(Text)
    link = Column(String(512), unique=True, index=True)
    pub_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
