"""Use case for creating a new course."""
from typing import Optional
from app.domain.entities.course import CourseEntity
from app.domain.repositories.course_repository import ICourseRepository


class CreateCourseUseCase:
    """Handles business logic for course creation."""

    def __init__(self, course_repo: ICourseRepository):
        self.course_repo = course_repo

    def execute(self, title: str, description: Optional[str], workload: int) -> CourseEntity:
        course = CourseEntity(
            id=None,
            title=title.strip(),
            description=description.strip() if description else None,
            workload=workload,
        )
        course.validate()
        return self.course_repo.create(course)
