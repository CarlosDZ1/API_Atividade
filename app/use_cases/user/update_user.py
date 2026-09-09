"""Use case for updating an existing user."""
from app.core.exceptions import DuplicateEntityException, EntityNotFoundException
from app.domain.entities.user import UserEntity
from app.domain.repositories.user_repository import IUserRepository


class UpdateUserUseCase:
    """Handles business logic for updating a user's details."""

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: int, name: str, email: str) -> UserEntity:
        existing_user = self.user_repo.get_by_id(user_id)
        if not existing_user:
            raise EntityNotFoundException(f"User with ID {user_id} not found.")

        normalized_email = email.strip().lower()

        # If email changed, verify it doesn't collide with another user
        if existing_user.email != normalized_email:
            user_with_email = self.user_repo.get_by_email(normalized_email)
            if user_with_email and user_with_email.id != user_id:
                raise DuplicateEntityException(f"Email '{normalized_email}' is already in use by another user.")

        updated_entity = UserEntity(
            id=user_id,
            name=name.strip(),
            email=normalized_email,
            created_at=existing_user.created_at,
        )
        updated_entity.validate()
        return self.user_repo.update(updated_entity)
