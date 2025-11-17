from datetime import datetime

from pydantic import BaseModel, EmailStr


class Profile(BaseModel):
    id: int | None = None
    username: str
    email: EmailStr
    bio: str | None = None
    created_at: datetime | None = None
