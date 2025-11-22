from __future__ import annotations

from typing import List

from news.domain.news import NewsArticle


class NewsService:
    def __init__(self, naver_client, news_repository):
        self.naver_client = naver_client
        self.news_repository = news_repository

    def fetch_and_store(self, query: str, display: int = 20, sort: str = "date") -> List[NewsArticle]:
        response = self.naver_client.search_news(query=query, display=display, sort=sort)
        items = response.get("items", []) if isinstance(response, dict) else []

        articles = [NewsArticle.from_naver_item(item) for item in items]
        return self.news_repository.save_all(articles)

    def get_latest(self, limit: int = 20) -> List[NewsArticle]:
        return self.news_repository.get_latest(limit)
