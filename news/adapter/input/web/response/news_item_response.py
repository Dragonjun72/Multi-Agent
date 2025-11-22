from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewsItemResponse(BaseModel):
    id: Optional[int]
    title: str
    description: str
    originallink: str
    link: str
    pub_date: Optional[datetime]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True