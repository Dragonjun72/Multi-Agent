from fastapi import APIRouter, Depends, HTTPException, Query

from account.application.factory.view_profile_usecase_factory import get_view_profile_usecase
from account.application.usecase.view_profile_usecase import ViewProfileUseCase

accountRouter = APIRouter()


@accountRouter.get("/profile/{profile_id}")
def get_profile(profile_id: int, usecase: ViewProfileUseCase = Depends(get_view_profile_usecase)):
    try:
        profile = usecase.execute(profile_id=profile_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    return profile


@accountRouter.get("/profile")
def get_profile_by_username(
    username: str = Query(None, description="조회할 사용자 이름"),
    usecase: ViewProfileUseCase = Depends(get_view_profile_usecase)
):
    if username is None:
        raise HTTPException(status_code=400, detail="username 쿼리 파라미터가 필요합니다.")

    try:
        profile = usecase.execute(username=username)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    return profile
