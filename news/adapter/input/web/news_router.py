from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database.session import get_db_session_dependency
from news.adapter.input.web.request.news_fetch_request import NewsFetchRequest
from news.adapter.input.web.response.news_item_response import NewsItemResponse
from news.application.usecase.news_usecase import NewsUseCase
from news.infrastructure.api.naver_news_client import NaverNewsClient
from news.infrastructure.repository.news_repository_impl import NewsRepositoryImpl

news_router = APIRouter(tags=["news"])


def get_news_usecase(session: Session = Depends(get_db_session_dependency)) -> NewsUseCase:
    client = NaverNewsClient()
    repository = NewsRepositoryImpl(session)
    return NewsUseCase(client, repository)


@news_router.post("/fetch", response_model=List[NewsItemResponse])
async def fetch_news(payload: NewsFetchRequest, usecase: NewsUseCase = Depends(get_news_usecase)):
    try:
        return usecase.fetch_and_store(payload.query, payload.display, payload.sort)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@news_router.get("/list", response_model=List[NewsItemResponse])
async def list_news(limit: int = 20, usecase: NewsUseCase = Depends(get_news_usecase)):
    try:
        return usecase.get_latest(limit)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc