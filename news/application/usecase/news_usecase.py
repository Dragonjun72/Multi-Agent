from typing import Iterable

from news.application.port.news_repository_port import NewsRepositoryPort
from news.domain.news import News


class NewsUseCase:
    def __init__(self, repository: NewsRepositoryPort):
        self.repository = repository

    def create_news(self, title: str, content: str) -> News:
        return self.repository.create_news(title, content)

    def list_news(self) -> Iterable[News]:
        return self.repository.list_news()
