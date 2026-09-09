"""Use case for enrolling a user into a course."""
from app.core.exceptions import DuplicateEntityException, EntityNotFoundException
from app.domain.entities.enrollment import EnrollmentEntity
from app.domain.repositories.user_repository import IUserRepository
from app.domain.repositories.course_repository import ICourseRepository
from app.domain.repositories.enrollment_repository import IEnrollmentRepository


class CreateEnrollmentUseCase:
    """Handles business logic for creating a course enrollment."""

    def __init__(
        self,
        enrollment_repo: IEnrollmentRepository,
        user_repo: IUserRepository,
        course_repo: ICourseRepository,
    ):
        self.enrollment_repo = enrollment_repo
        self.user_repo = user_repo
        self.course_repo = course_repo

    def execute(self, user_id: int, course_id: int) -> EnrollmentEntity:
        # 1. Validate if user exists
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise EntityNotFoundException(f"User with ID {user_id} not found.")

        # 2. Validate if course exists
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise EntityNotFoundException(f"Course with ID {course_id} not found.")

        # 3. Check for duplicate enrollment
        existing_enrollment = self.enrollment_repo.find_by_user_and_course(user_id, course_id)
        if existing_enrollment:
            raise DuplicateEntityException(
                f"User {user_id} is already enrolled in course '{course.title}' (ID {course_id})."
            )

        # 4. Create and persist enrollment
        enrollment = EnrollmentEntity(id=None, user_id=user_id, course_id=course_id)
        enrollment.validate()
        return self.enrollment_repo.create(enrollment)
