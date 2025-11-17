from account.domain.entity.profile import Profile
from account.domain.port.profile_repository_port import ProfileRepositoryPort


class ViewProfileUseCase:
    def __init__(self, profile_repository: ProfileRepositoryPort):
        self.profile_repository = profile_repository

    def execute(self, profile_id: int | None = None, username: str | None = None) -> Profile:
        if profile_id is None and username is None:
            raise ValueError("profile_id 또는 username 중 하나는 필요합니다.")

        profile: Profile | None = None
        if profile_id is not None:
            profile = self.profile_repository.find_by_id(profile_id)
        elif username is not None:
            profile = self.profile_repository.find_by_username(username)

        if profile is None:
            raise ValueError("요청한 프로필을 찾을 수 없습니다.")

        return profile
