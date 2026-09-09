"""Use case for deleting a course."""
from app.core.exceptions import EntityNotFoundException
from app.domain.repositories.course_repository import ICourseRepository


class DeleteCourseUseCase:
    """Handles business logic for deleting a course."""

    def __init__(self, course_repo: ICourseRepository):
        self.course_repo = course_repo

    def execute(self, course_id: int) -> bool:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise EntityNotFoundException(f"Course with ID {course_id} not found.")
        return self.course_repo.delete(course_id)
