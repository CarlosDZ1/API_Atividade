"""Use case for listing all users."""
from typing import List
from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import IUserRepository


class ListUsersUseCase:
    """Handles business logic for retrieving all users."""

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self) -> List[UserEntity]:
        return self.user_repo.list_all()
