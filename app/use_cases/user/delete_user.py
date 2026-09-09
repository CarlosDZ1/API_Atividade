"""Use case for deleting a user."""
from app.core.exceptions import EntityNotFoundException
from app.domain.repositories.user_repository import IUserRepository


class DeleteUserUseCase:
    """Handles business logic for removing a user."""

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: int) -> bool:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise EntityNotFoundException(f"User with ID {user_id} not found.")
        return self.user_repo.delete(user_id)
