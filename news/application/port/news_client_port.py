from typing import Protocol


class NewsClientPort(Protocol):
    def search_news(self, query: str, display: int = 20, sort: str = "date") -> list[dict]:
        ...