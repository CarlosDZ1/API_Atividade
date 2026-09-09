"""Use case for retrieving a single course by ID."""
from app.core.exceptions import EntityNotFoundException
from app.domain.entities.course import CourseEntity
from app.domain.repositories.course_repository import ICourseRepository


class GetCourseUseCase:
    """Handles business logic for retrieving a course by identifier."""

    def __init__(self, course_repo: ICourseRepository):
        self.course_repo = course_repo

    def execute(self, course_id: int) -> CourseEntity:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise EntityNotFoundException(f"Course with ID {course_id} not found.")
        return course
