from account.adapter.output.persistence.profile_repository_adapter import ProfileRepositoryAdapter
from account.application.usecase.view_profile_usecase import ViewProfileUseCase


def get_view_profile_usecase():
    repository = ProfileRepositoryAdapter()
    return ViewProfileUseCase(repository)
