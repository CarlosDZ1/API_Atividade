"""Use case for retrieving a user and all courses they are enrolled in."""
from typing import Dict, Any
from app.core.exceptions import EntityNotFoundException
from app.domain.repositories.user_repository import IUserRepository


class GetUserCoursesUseCase:
    """Handles business logic for retrieving a user with their enrolled courses."""

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: int) -> Dict[str, Any]:
        result = self.user_repo.get_user_with_courses(user_id)
        if not result:
            raise EntityNotFoundException(f"User with ID {user_id} not found.")

        user_entity, course_entities = result
        return {
            "user": user_entity,
            "courses": course_entities,
        }
