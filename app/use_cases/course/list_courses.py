"""Use case for listing all courses."""
from typing import List
from app.domain.entities.course import CourseEntity
from app.domain.repositories.course_repository import ICourseRepository


class ListCoursesUseCase:
    """Handles business logic for retrieving all courses."""

    def __init__(self, course_repo: ICourseRepository):
        self.course_repo = course_repo

    def execute(self) -> List[CourseEntity]:
        return self.course_repo.list_all()
