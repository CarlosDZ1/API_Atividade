"""Dependency injection providers for repositories and use cases."""
from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database.session import get_db

# Repositories
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.infrastructure.repositories.course_repository_impl import CourseRepositoryImpl
from app.infrastructure.repositories.enrollment_repository_impl import EnrollmentRepositoryImpl

# User Use Cases
from app.use_cases.user.create_user import CreateUserUseCase
from app.use_cases.user.list_users import ListUsersUseCase
from app.use_cases.user.get_user import GetUserUseCase
from app.use_cases.user.update_user import UpdateUserUseCase
from app.use_cases.user.delete_user import DeleteUserUseCase
from app.use_cases.user.get_user_courses import GetUserCoursesUseCase

# Course Use Cases
from app.use_cases.course.create_course import CreateCourseUseCase
from app.use_cases.course.list_courses import ListCoursesUseCase
from app.use_cases.course.get_course import GetCourseUseCase
from app.use_cases.course.update_course import UpdateCourseUseCase
from app.use_cases.course.delete_course import DeleteCourseUseCase

# Enrollment Use Cases
from app.use_cases.enrollment.create_enrollment import CreateEnrollmentUseCase


# --- Repositories Providers ---

def get_user_repository(db: Session = Depends(get_db)) -> UserRepositoryImpl:
    return UserRepositoryImpl(db)


def get_course_repository(db: Session = Depends(get_db)) -> CourseRepositoryImpl:
    return CourseRepositoryImpl(db)


def get_enrollment_repository(db: Session = Depends(get_db)) -> EnrollmentRepositoryImpl:
    return EnrollmentRepositoryImpl(db)


# --- User Use Case Providers ---

def get_create_user_use_case(
    repo: UserRepositoryImpl = Depends(get_user_repository),
) -> CreateUserUseCase:
    return CreateUserUseCase(repo)


def get_list_users_use_case(
    repo: UserRepositoryImpl = Depends(get_user_repository),
) -> ListUsersUseCase:
    return ListUsersUseCase(repo)


def get_get_user_use_case(
    repo: UserRepositoryImpl = Depends(get_user_repository),
) -> GetUserUseCase:
    return GetUserUseCase(repo)


def get_update_user_use_case(
    repo: UserRepositoryImpl = Depends(get_user_repository),
) -> UpdateUserUseCase:
    return UpdateUserUseCase(repo)


def get_delete_user_use_case(
    repo: UserRepositoryImpl = Depends(get_user_repository),
) -> DeleteUserUseCase:
    return DeleteUserUseCase(repo)


def get_user_courses_use_case(
    repo: UserRepositoryImpl = Depends(get_user_repository),
) -> GetUserCoursesUseCase:
    return GetUserCoursesUseCase(repo)


# --- Course Use Case Providers ---

def get_create_course_use_case(
    repo: CourseRepositoryImpl = Depends(get_course_repository),
) -> CreateCourseUseCase:
    return CreateCourseUseCase(repo)


def get_list_courses_use_case(
    repo: CourseRepositoryImpl = Depends(get_course_repository),
) -> ListCoursesUseCase:
    return ListCoursesUseCase(repo)


def get_get_course_use_case(
    repo: CourseRepositoryImpl = Depends(get_course_repository),
) -> GetCourseUseCase:
    return GetCourseUseCase(repo)


def get_update_course_use_case(
    repo: CourseRepositoryImpl = Depends(get_course_repository),
) -> UpdateCourseUseCase:
    return UpdateCourseUseCase(repo)


def get_delete_course_use_case(
    repo: CourseRepositoryImpl = Depends(get_course_repository),
) -> DeleteCourseUseCase:
    return DeleteCourseUseCase(repo)


# --- Enrollment Use Case Providers ---

def get_create_enrollment_use_case(
    enrollment_repo: EnrollmentRepositoryImpl = Depends(get_enrollment_repository),
    user_repo: UserRepositoryImpl = Depends(get_user_repository),
    course_repo: CourseRepositoryImpl = Depends(get_course_repository),
) -> CreateEnrollmentUseCase:
    return CreateEnrollmentUseCase(enrollment_repo, user_repo, course_repo)
