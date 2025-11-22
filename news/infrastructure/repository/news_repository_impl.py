from typing import Iterable, List

from sqlalchemy.orm import Session

from config.database.session import get_db_session
from news.application.port.news_repository_port import NewsRepositoryPort
from news.domain.news import News
from news.infrastructure.orm.news_orm import NewsORM


class NewsRepositoryImpl(NewsRepositoryPort):
    def __init__(self):
        self.db: Session = get_db_session()

    def create_news(self, title: str, content: str) -> News:
        news_record = NewsORM(title=title, content=content)
        self.db.add(news_record)
        self.db.commit()
        self.db.refresh(news_record)
        return self._to_domain(news_record)

    def list_news(self) -> Iterable[News]:
        records: List[NewsORM] = (
            self.db.query(NewsORM).order_by(NewsORM.created_at.desc()).all()
        )
        return [self._to_domain(record) for record in records]

    @staticmethod
    def _to_domain(record: NewsORM) -> News:
        return News(
            id=record.id,
            title=record.title,
            content=record.content,
            created_at=record.created_at,
        )
