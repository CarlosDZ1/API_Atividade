"""SQLAlchemy implementation of IEnrollmentRepository."""
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.domain.entities.enrollment import EnrollmentEntity
from app.domain.repositories.enrollment_repository import IEnrollmentRepository
from app.infrastructure.database.models import EnrollmentModel


class EnrollmentRepositoryImpl(IEnrollmentRepository):
    """Concrete repository for Enrollment persistence using SQLAlchemy."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, enrollment: EnrollmentEntity) -> EnrollmentEntity:
        model = EnrollmentModel(
            user_id=enrollment.user_id,
            course_id=enrollment.course_id,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model.to_domain()

    def find_by_user_and_course(self, user_id: int, course_id: int) -> Optional[EnrollmentEntity]:
        stmt = select(EnrollmentModel).where(
            EnrollmentModel.user_id == user_id,
            EnrollmentModel.course_id == course_id,
        )
        model = self.db.scalars(stmt).first()
        return model.to_domain() if model else None

    def list_by_user(self, user_id: int) -> List[EnrollmentEntity]:
        stmt = select(EnrollmentModel).where(EnrollmentModel.user_id == user_id)
        models = self.db.scalars(stmt).all()
        return [m.to_domain() for m in models]

    def list_by_course(self, course_id: int) -> List[EnrollmentEntity]:
        stmt = select(EnrollmentModel).where(EnrollmentModel.course_id == course_id)
        models = self.db.scalars(stmt).all()
        return [m.to_domain() for m in models]
