"""SQLAlchemy implementation of IUserRepository."""
from typing import List, Optional, Tuple
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.domain.entities.user import UserEntity
from app.domain.entities.course import CourseEntity
from app.domain.repositories.user_repository import IUserRepository
from app.infrastructure.database.models import UserModel, CourseModel, EnrollmentModel


class UserRepositoryImpl(IUserRepository):
    """Concrete repository for User persistence using SQLAlchemy."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserEntity) -> UserEntity:
        model = UserModel(name=user.name, email=user.email)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model.to_domain()

    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        stmt = select(UserModel).where(UserModel.id == user_id)
        model = self.db.scalars(stmt).first()
        return model.to_domain() if model else None

    def get_by_email(self, email: str) -> Optional[UserEntity]:
        stmt = select(UserModel).where(UserModel.email == email)
        model = self.db.scalars(stmt).first()
        return model.to_domain() if model else None

    def list_all(self) -> List[UserEntity]:
        stmt = select(UserModel).order_by(UserModel.id)
        models = self.db.scalars(stmt).all()
        return [m.to_domain() for m in models]

    def update(self, user: UserEntity) -> UserEntity:
        stmt = select(UserModel).where(UserModel.id == user.id)
        model = self.db.scalars(stmt).first()
        if not model:
            raise ValueError(f"User with ID {user.id} not found.")
        model.name = user.name
        model.email = user.email
        self.db.commit()
        self.db.refresh(model)
        return model.to_domain()

    def delete(self, user_id: int) -> bool:
        stmt = select(UserModel).where(UserModel.id == user_id)
        model = self.db.scalars(stmt).first()
        if not model:
            return False
        self.db.delete(model)
        self.db.commit()
        return True

    def get_user_with_courses(self, user_id: int) -> Optional[Tuple[UserEntity, List[CourseEntity]]]:
        """Loads user and their enrolled courses using ORM relationships."""
        stmt = (
            select(UserModel)
            .where(UserModel.id == user_id)
            .options(selectinload(UserModel.enrollments).selectinload(EnrollmentModel.course))
        )
        model = self.db.scalars(stmt).first()
        if not model:
            return None

        user_entity = model.to_domain()
        courses = [
            enrollment.course.to_domain()
            for enrollment in model.enrollments
            if enrollment.course is not None
        ]
        return user_entity, courses
