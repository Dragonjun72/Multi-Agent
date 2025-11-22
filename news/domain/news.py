from __future__ import annotations

import html
import re
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import Optional


class NewsArticle:
    def __init__(
        self,
        title: str,
        description: str,
        originallink: str,
        link: str,
        pub_date: datetime,
    ):
        self.id: Optional[int] = None
        self.title = title
        self.description = description
        self.originallink = originallink
        self.link = link
        self.pub_date = pub_date

    @classmethod
    def from_naver_item(cls, item: dict) -> "NewsArticle":
        title = cls._clean_text(item.get("title", ""))
        description = cls._clean_text(item.get("description", ""))
        originallink = item.get("originallink", "")
        link = item.get("link", "")
        pub_date = cls._parse_pub_date(item.get("pubDate"))

        return cls(title, description, originallink, link, pub_date)

    @staticmethod
    def _clean_text(text: str) -> str:
        cleaned = re.sub(r"<[^>]+>", "", text or "")
        return html.unescape(cleaned).strip()

    @staticmethod
    def _parse_pub_date(pub_date: Optional[str]) -> datetime:
        if not pub_date:
            return datetime.utcnow()

        try:
            return parsedate_to_datetime(pub_date)
        except (TypeError, ValueError):
            return datetime.utcnow()
