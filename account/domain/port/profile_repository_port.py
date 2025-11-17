from abc import ABC, abstractmethod

from account.domain.entity.profile import Profile


class ProfileRepositoryPort(ABC):
    @abstractmethod
    def find_by_id(self, profile_id: int) -> Profile | None:
        """ID로 프로필 조회"""
        raise NotImplementedError

    @abstractmethod
    def find_by_username(self, username: str) -> Profile | None:
        """사용자 이름으로 프로필 조회"""
        raise NotImplementedError
