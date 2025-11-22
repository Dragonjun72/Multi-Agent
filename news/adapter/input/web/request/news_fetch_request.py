from pydantic import BaseModel, Field


class NewsFetchRequest(BaseModel):
    query: str = Field(..., description="검색할 키워드")
    display: int = Field(20, ge=1, le=100, description="가져올 뉴스 개수")
    sort: str = Field("date", description="정렬 방식(sim 또는 date)")