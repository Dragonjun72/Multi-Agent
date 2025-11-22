from typing import List

from news.application.port.news_client_port import NewsClientPort
from news.application.port.news_repository_port import NewsRepositoryPort
from news.domain.news import News


class NewsUseCase:
    def __init__(self, news_client: NewsClientPort, repository: NewsRepositoryPort):
        self.news_client = news_client
        self.repository = repository

    def fetch_and_store(self, query: str, display: int = 20, sort: str = "date") -> List[News]:
        raw_items = self.news_client.search_news(query=query, display=display, sort=sort)
        news_list = [News.from_naver_payload(item) for item in raw_items]
        return self.repository.upsert_many(news_list)

    def get_latest(self, limit: int = 20) -> List[News]:
        return self.repository.list_latest(limit=limit)