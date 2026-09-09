"""Abstract interface for Course repository."""
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.course import CourseEntity


class ICourseRepository(ABC):
    """Interface defining operations on the Course persistence layer."""

    @abstractmethod
    def create(self, course: CourseEntity) -> CourseEntity:
        """Persist a new course."""
        pass

    @abstractmethod
    def get_by_id(self, course_id: int) -> Optional[CourseEntity]:
        """Find course by ID."""
        pass

    @abstractmethod
    def list_all(self) -> List[CourseEntity]:
        """Retrieve all courses."""
        pass

    @abstractmethod
    def update(self, course: CourseEntity) -> CourseEntity:
        """Update existing course."""
        pass

    @abstractmethod
    def delete(self, course_id: int) -> bool:
        """Delete course by ID."""
        pass
