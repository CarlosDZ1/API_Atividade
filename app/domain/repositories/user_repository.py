"""Abstract interface for User repository."""
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from app.domain.entities.user import UserEntity
from app.domain.entities.course import CourseEntity


class IUserRepository(ABC):
    """Interface defining operations on the User persistence layer."""

    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        """Persist a new user."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        """Find user by ID."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserEntity]:
        """Find user by unique email."""
        pass

    @abstractmethod
    def list_all(self) -> List[UserEntity]:
        """Retrieve all users."""
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity:
        """Update existing user."""
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """Delete user by ID."""
        pass

    @abstractmethod
    def get_user_with_courses(self, user_id: int) -> Optional[Tuple[UserEntity, List[CourseEntity]]]:
        """Retrieve user together with the list of enrolled courses."""
        pass
