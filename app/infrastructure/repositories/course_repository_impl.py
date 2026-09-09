"""SQLAlchemy implementation of ICourseRepository."""
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.domain.entities.course import CourseEntity
from app.domain.repositories.course_repository import ICourseRepository
from app.infrastructure.database.models import CourseModel


class CourseRepositoryImpl(ICourseRepository):
    """Concrete repository for Course persistence using SQLAlchemy."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, course: CourseEntity) -> CourseEntity:
        model = CourseModel(
            title=course.title,
            description=course.description,
            workload=course.workload,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model.to_domain()

    def get_by_id(self, course_id: int) -> Optional[CourseEntity]:
        stmt = select(CourseModel).where(CourseModel.id == course_id)
        model = self.db.scalars(stmt).first()
        return model.to_domain() if model else None

    def list_all(self) -> List[CourseEntity]:
        stmt = select(CourseModel).order_by(CourseModel.id)
        models = self.db.scalars(stmt).all()
        return [m.to_domain() for m in models]

    def update(self, course: CourseEntity) -> CourseEntity:
        stmt = select(CourseModel).where(CourseModel.id == course.id)
        model = self.db.scalars(stmt).first()
        if not model:
            raise ValueError(f"Course with ID {course.id} not found.")
        model.title = course.title
        model.description = course.description
        model.workload = course.workload
        self.db.commit()
        self.db.refresh(model)
        return model.to_domain()

    def delete(self, course_id: int) -> bool:
        stmt = select(CourseModel).where(CourseModel.id == course_id)
        model = self.db.scalars(stmt).first()
        if not model:
            return False
        self.db.delete(model)
        self.db.commit()
        return True
