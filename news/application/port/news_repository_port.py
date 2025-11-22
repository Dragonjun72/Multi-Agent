from abc import ABC, abstractmethod
from typing import Iterable

from news.domain.news import News


class NewsRepositoryPort(ABC):

    @abstractmethod
    def create_news(self, title: str, content: str) -> News:
        raise NotImplementedError

    @abstractmethod
    def list_news(self) -> Iterable[News]:
        raise NotImplementedError
