from dataclasses import dataclass
from datetime import datetime


@dataclass
class News:
    id: int
    title: str
    content: str
    created_at: datetime
