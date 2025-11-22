from typing import List, Protocol

from news.domain.news import News


class NewsRepositoryPort(Protocol):
    def upsert_many(self, news_list: List[News]) -> List[News]:
        ...

    def list_latest(self, limit: int = 20) -> List[News]:
        ...