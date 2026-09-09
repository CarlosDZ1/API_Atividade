"""Use case for creating a new user."""
from app.core.exceptions import DuplicateEntityException
from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import IUserRepository


class CreateUserUseCase:
    """Handles business logic for user registration."""

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, name: str, email: str) -> UserEntity:
        # Check if email is already taken
        existing_user = self.user_repo.get_by_email(email)
        if existing_user:
            raise DuplicateEntityException(f"User with email '{email}' already exists.")

        user = UserEntity(id=None, name=name.strip(), email=email.strip().lower())
        user.validate()
        return self.user_repo.create(user)
