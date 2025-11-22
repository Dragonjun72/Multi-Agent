import os
from typing import Any, Dict, Optional

import requests

NAVER_NEWS_SEARCH_URL = "https://openapi.naver.com/v1/search/news.json"
NAVER_CLIENT_ID_HEADER = "X-Naver-Client-Id"
NAVER_CLIENT_SECRET_HEADER = "X-Naver-Client-Secret"


class NaverClientError(Exception):
    """Base exception for Naver news client errors."""


class NaverClientAuthError(NaverClientError):
    """Raised when credentials are missing or invalid."""


class NaverClientResponseError(NaverClientError):
    """Raised when Naver API returns an error response."""

    def __init__(self, status_code: int, message: str):
        super().__init__(f"Naver API error {status_code}: {message}")
        self.status_code = status_code
        self.message = message


def _build_headers() -> Dict[str, str]:
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise NaverClientAuthError("NAVER client credentials are not configured.")

    return {
        NAVER_CLIENT_ID_HEADER: client_id,
        NAVER_CLIENT_SECRET_HEADER: client_secret,
    }


def _handle_response(response: requests.Response) -> Dict[str, Any]:
    if response.ok:
        return response.json()

    try:
        detail = response.json()
    except ValueError:
        detail = response.text

    raise NaverClientResponseError(response.status_code, str(detail))


def search_news(
    query: Optional[str] = None,
    display: int = 20,
    sort: Optional[str] = None,
    start: int = 1,
    timeout: int = 10,
) -> Dict[str, Any]:
    effective_query = query or os.getenv("NAVER_NEWS_DEFAULT_QUERY")
    effective_sort = sort or os.getenv("NAVER_NEWS_DEFAULT_SORT", "date")

    if not effective_query:
        raise NaverClientError("Search query is required.")

    params = {
        "query": effective_query,
        "display": display,
        "sort": effective_sort,
        "start": start,
    }

    response = requests.get(
        NAVER_NEWS_SEARCH_URL,
        headers=_build_headers(),
        params=params,
        timeout=timeout,
    )

    return _handle_response(response)
