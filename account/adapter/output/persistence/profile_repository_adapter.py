from account.adapter.output.persistence.profile_orm import ProfileORM
from account.domain.entity.profile import Profile
from account.domain.port.profile_repository_port import ProfileRepositoryPort
from account.infrastructure.config.mysql_config import AccountSessionLocal


class ProfileRepositoryAdapter(ProfileRepositoryPort):
    def find_by_id(self, profile_id: int) -> Profile | None:
        session = AccountSessionLocal()
        try:
            orm_profile = session.get(ProfileORM, profile_id)
            if orm_profile is None:
                return None

            return Profile(
                id=orm_profile.id,
                username=orm_profile.username,
                email=orm_profile.email,
                bio=orm_profile.bio,
                created_at=orm_profile.created_at,
            )
        finally:
            session.close()

    def find_by_username(self, username: str) -> Profile | None:
        session = AccountSessionLocal()
        try:
            orm_profile = session.query(ProfileORM).filter_by(username=username).first()
            if orm_profile is None:
                return None

            return Profile(
                id=orm_profile.id,
                username=orm_profile.username,
                email=orm_profile.email,
                bio=orm_profile.bio,
                created_at=orm_profile.created_at,
            )
        finally:
            session.close()
