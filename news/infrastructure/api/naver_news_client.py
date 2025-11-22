import os
from typing import Any, Dict, List

import requests

from news.application.port.news_client_port import NewsClientPort


class NaverNewsClient(NewsClientPort):
    BASE_URL = "https://openapi.naver.com/v1/search/news.json"

    def __init__(self, session: requests.Session | None = None):
        self.client_id = os.getenv("NAVER_CLIENT_ID")
        self.client_secret = os.getenv("NAVER_CLIENT_SECRET")
        self.session = session or requests.Session()

    def search_news(self, query: str, display: int = 20, sort: str = "date") -> List[Dict[str, Any]]:
        if not self.client_id or not self.client_secret:
            raise ValueError("NAVER client credentials are not configured")

        headers = {
            "X-Naver-Client-Id": self.client_id,
            "X-Naver-Client-Secret": self.client_secret,
        }
        params = {
            "query": query,
            "display": display,
            "sort": sort,
        }

        try:
            response = self.session.get(self.BASE_URL, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            body = response.json()
        except requests.RequestException as exc:
            raise ValueError(f"Failed to fetch news from Naver: {exc}") from exc

        return body.get("items", [])