from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Optional


class News:
    def __init__(
        self,
        title: str,
        description: str,
        originallink: str,
        link: str,
        pub_date: Optional[datetime] = None,
    ):
        if not title:
            raise ValueError("title is required")
        if not link:
            raise ValueError("link is required")

        self.id: Optional[int] = None
        self.title = title
        self.description = description
        self.originallink = originallink
        self.link = link
        self.pub_date = pub_date
        self.created_at: Optional[datetime] = None

    @classmethod
    def from_naver_payload(cls, payload: dict[str, str]) -> "News":
        pub_date = cls._parse_pub_date(payload.get("pubDate"))
        return cls(
            title=payload.get("title", ""),
            description=payload.get("description", ""),
            originallink=payload.get("originallink", ""),
            link=payload.get("link", ""),
            pub_date=pub_date,
        )

    @staticmethod
    def _parse_pub_date(pub_date: Optional[str]) -> Optional[datetime]:
        if not pub_date:
            return None
        try:
            dt = parsedate_to_datetime(pub_date)
            if dt is None:
                return None
            if dt.tzinfo:
                return dt.astimezone(timezone.utc).replace(tzinfo=None)
            return dt
        except Exception:
            return None