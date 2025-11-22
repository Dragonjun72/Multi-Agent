from datetime import datetime
from typing import List

from pydantic import BaseModel


class NewsResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime


class NewsListResponse(BaseModel):
    items: List[NewsResponse]
