from typing import List

from fastapi import APIRouter

from news.adapter.input.web.request.create_news_request import CreateNewsRequest
from news.adapter.input.web.response.news_response import NewsListResponse, NewsResponse
from news.application.usecase.news_usecase import NewsUseCase
from news.infrastructure.repository.news_repository_impl import NewsRepositoryImpl

news_router = APIRouter(tags=["news"])
news_usecase = NewsUseCase(NewsRepositoryImpl())


@news_router.post("/create", response_model=NewsResponse)
def create_news(payload: CreateNewsRequest) -> NewsResponse:
    news = news_usecase.create_news(payload.title, payload.content)
    return NewsResponse(
        id=news.id,
        title=news.title,
        content=news.content,
        created_at=news.created_at,
    )


@news_router.get("/list", response_model=NewsListResponse)
def list_news() -> NewsListResponse:
    news_list = news_usecase.list_news()
    items: List[NewsResponse] = [
        NewsResponse(
            id=news.id,
            title=news.title,
            content=news.content,
            created_at=news.created_at,
        )
        for news in news_list
    ]
    return NewsListResponse(items=items)
