"""Use case for retrieving a single user by ID."""
from app.core.exceptions import EntityNotFoundException
from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import IUserRepository


class GetUserUseCase:
    """Handles business logic for retrieving a user by identifier."""

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: int) -> UserEntity:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise EntityNotFoundException(f"User with ID {user_id} not found.")
        return user
