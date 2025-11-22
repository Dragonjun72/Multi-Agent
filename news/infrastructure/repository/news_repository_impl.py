from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from news.application.port.news_repository_port import NewsRepositoryPort
from news.domain.news import News
from news.infrastructure.orm.news_orm import NewsORM


class NewsRepositoryImpl(NewsRepositoryPort):
    def __init__(self, session: Session):
        self.session = session

    def upsert_many(self, news_list: List[News]) -> List[News]:
        stored: List[News] = []
        for item in news_list:
            existing = self.session.query(NewsORM).filter(NewsORM.link == item.link).first()
            if existing:
                existing.title = item.title
                existing.description = item.description
                existing.originallink = item.originallink
                existing.pub_date = item.pub_date
                self.session.add(existing)
                self.session.flush()
                stored.append(self._to_domain(existing))
                continue

            orm = NewsORM(
                title=item.title,
                description=item.description,
                originallink=item.originallink,
                link=item.link,
                pub_date=item.pub_date,
            )
            self.session.add(orm)
            self.session.flush()
            stored.append(self._to_domain(orm))

        self.session.commit()
        return stored

    def list_latest(self, limit: int = 20) -> List[News]:
        query = self.session.query(NewsORM).order_by(desc(NewsORM.pub_date), desc(NewsORM.created_at)).limit(limit)
        return [self._to_domain(orm) for orm in query.all()]

    @staticmethod
    def _to_domain(orm: NewsORM) -> News:
        news = News(
            title=orm.title,
            description=orm.description,
            originallink=orm.originallink,
            link=orm.link,
            pub_date=orm.pub_date,
        )
        news.id = orm.id
        news.created_at = orm.created_at
        return news