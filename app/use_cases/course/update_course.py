"""Use case for updating an existing course."""
from typing import Optional
from app.core.exceptions import EntityNotFoundException
from app.domain.entities.course import CourseEntity
from app.domain.repositories.course_repository import ICourseRepository


class UpdateCourseUseCase:
    """Handles business logic for updating a course."""

    def __init__(self, course_repo: ICourseRepository):
        self.course_repo = course_repo

    def execute(self, course_id: int, title: str, description: Optional[str], workload: int) -> CourseEntity:
        existing_course = self.course_repo.get_by_id(course_id)
        if not existing_course:
            raise EntityNotFoundException(f"Course with ID {course_id} not found.")

        updated_entity = CourseEntity(
            id=course_id,
            title=title.strip(),
            description=description.strip() if description else None,
            workload=workload,
        )
        updated_entity.validate()
        return self.course_repo.update(updated_entity)
