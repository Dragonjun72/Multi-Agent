from typing import Iterable, List, Sequence

from sqlalchemy.orm import Session

from news.domain.news_model import NewsModel


class NewsRepository:
    def __init__(self, db: Session):
        self.db = db

    def upsert_news_items(self, news_items: Sequence[dict]) -> List[NewsModel]:
        saved_items: List[NewsModel] = []

        for item in news_items:
            link = item.get("link")
            if not link:
                continue

            existing = self.db.query(NewsModel).filter(NewsModel.link == link).first()
            if existing:
                updated_fields = False
                if "title" in item and item["title"] != existing.title:
                    existing.title = item["title"]
                    updated_fields = True
                if "description" in item and item["description"] != existing.description:
                    existing.description = item["description"]
                    updated_fields = True
                if "pub_date" in item and item["pub_date"] != existing.pub_date:
                    existing.pub_date = item["pub_date"]
                    updated_fields = True

                if updated_fields:
                    self.db.add(existing)
                saved_items.append(existing)
                continue

            news = NewsModel(
                title=item.get("title"),
                description=item.get("description"),
                link=link,
                pub_date=item.get("pub_date"),
            )
            self.db.add(news)
            saved_items.append(news)

        self.db.commit()
        for item in saved_items:
            self.db.refresh(item)

        return saved_items

    def list_news(self) -> Iterable[NewsModel]:
        return self.db.query(NewsModel).order_by(NewsModel.pub_date.desc()).all()
