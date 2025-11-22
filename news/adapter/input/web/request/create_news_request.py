from pydantic import BaseModel


class CreateNewsRequest(BaseModel):
    title: str
    content: str
