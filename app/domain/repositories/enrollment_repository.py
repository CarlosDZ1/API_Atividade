"""Abstract interface for Enrollment repository."""
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.enrollment import EnrollmentEntity


class IEnrollmentRepository(ABC):
    """Interface defining operations on the Enrollment persistence layer."""

    @abstractmethod
    def create(self, enrollment: EnrollmentEntity) -> EnrollmentEntity:
        """Persist a new enrollment."""
        pass

    @abstractmethod
    def find_by_user_and_course(self, user_id: int, course_id: int) -> Optional[EnrollmentEntity]:
        """Check if an enrollment already exists for a user and course."""
        pass

    @abstractmethod
    def list_by_user(self, user_id: int) -> List[EnrollmentEntity]:
        """List all enrollments for a user."""
        pass

    @abstractmethod
    def list_by_course(self, course_id: int) -> List[EnrollmentEntity]:
        """List all enrollments for a course."""
        pass
