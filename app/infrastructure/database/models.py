"""SQLAlchemy 2.0 ORM Models."""
from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.database.session import Base
from app.domain.entities.user import UserEntity
from app.domain.entities.course import CourseEntity
from app.domain.entities.enrollment import EnrollmentEntity


class UserModel(Base):
    """Database model for Users."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationships
    enrollments: Mapped[List["EnrollmentModel"]] = relationship(
        "EnrollmentModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def to_domain(self) -> UserEntity:
        """Convert ORM model to pure domain entity."""
        return UserEntity(
            id=self.id,
            name=self.name,
            email=self.email,
            created_at=self.created_at,
        )


class CourseModel(Base):
    """Database model for Courses."""

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    workload: Mapped[int] = mapped_column(Integer, nullable=False)

    # Relationships
    enrollments: Mapped[List["EnrollmentModel"]] = relationship(
        "EnrollmentModel",
        back_populates="course",
        cascade="all, delete-orphan",
    )

    def to_domain(self) -> CourseEntity:
        """Convert ORM model to pure domain entity."""
        return CourseEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            workload=self.workload,
        )


class EnrollmentModel(Base):
    """Database model for Enrollments."""

    __tablename__ = "enrollments"
    __table_args__ = (
        UniqueConstraint("user_id", "course_id", name="uq_user_course_enrollment"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    course_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("courses.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    enrolled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationships
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="enrollments")
    course: Mapped["CourseModel"] = relationship("CourseModel", back_populates="enrollments")

    def to_domain(self) -> EnrollmentEntity:
        """Convert ORM model to pure domain entity."""
        return EnrollmentEntity(
            id=self.id,
            user_id=self.user_id,
            course_id=self.course_id,
            enrolled_at=self.enrolled_at,
        )
