"""User presentation controller/router."""
from typing import List
from fastapi import APIRouter, Depends, status
from app.presentation.schemas.common import ApiResponse
from app.presentation.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse,
    UserCoursesResponse,
)
from app.presentation.schemas.course_schema import CourseResponse
from app.presentation.dependencies import (
    get_create_user_use_case,
    get_list_users_use_case,
    get_get_user_use_case,
    get_update_user_use_case,
    get_delete_user_use_case,
    get_user_courses_use_case,
)
from app.use_cases.user.create_user import CreateUserUseCase
from app.use_cases.user.list_users import ListUsersUseCase
from app.use_cases.user.get_user import GetUserUseCase
from app.use_cases.user.update_user import UpdateUserUseCase
from app.use_cases.user.delete_user import DeleteUserUseCase
from app.use_cases.user.get_user_courses import GetUserCoursesUseCase

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ApiResponse[UserResponse],
    summary="Create a new user",
)
def create_user(
    payload: UserCreate,
    use_case: CreateUserUseCase = Depends(get_create_user_use_case),
):
    created_user = use_case.execute(name=payload.name, email=payload.email)
    return ApiResponse(
        success=True,
        message="User created successfully",
        data=UserResponse(
            id=created_user.id,
            name=created_user.name,
            email=created_user.email,
            created_at=created_user.created_at,
        ),
    )


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[List[UserResponse]],
    summary="List all users",
)
def list_users(
    use_case: ListUsersUseCase = Depends(get_list_users_use_case),
):
    users = use_case.execute()
    data = [
        UserResponse(
            id=u.id,
            name=u.name,
            email=u.email,
            created_at=u.created_at,
        )
        for u in users
    ]
    return ApiResponse(
        success=True,
        message="Users retrieved successfully",
        data=data,
    )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[UserResponse],
    summary="Get user by ID",
)
def get_user(
    id: int,
    use_case: GetUserUseCase = Depends(get_get_user_use_case),
):
    user = use_case.execute(user_id=id)
    return ApiResponse(
        success=True,
        message="User retrieved successfully",
        data=UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
        ),
    )


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[UserResponse],
    summary="Update user by ID",
)
def update_user(
    id: int,
    payload: UserUpdate,
    use_case: UpdateUserUseCase = Depends(get_update_user_use_case),
):
    updated_user = use_case.execute(user_id=id, name=payload.name, email=payload.email)
    return ApiResponse(
        success=True,
        message="User updated successfully",
        data=UserResponse(
            id=updated_user.id,
            name=updated_user.name,
            email=updated_user.email,
            created_at=updated_user.created_at,
        ),
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[None],
    summary="Delete user by ID",
)
def delete_user(
    id: int,
    use_case: DeleteUserUseCase = Depends(get_delete_user_use_case),
):
    use_case.execute(user_id=id)
    return ApiResponse(
        success=True,
        message="User deleted successfully",
        data=None,
    )


@router.get(
    "/{id}/courses",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[UserCoursesResponse],
    summary="Get user and their enrolled courses",
)
def get_user_courses(
    id: int,
    use_case: GetUserCoursesUseCase = Depends(get_user_courses_use_case),
):
    result = use_case.execute(user_id=id)
    user = result["user"]
    courses = result["courses"]

    user_response = UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        created_at=user.created_at,
    )
    course_responses = [
        CourseResponse(
            id=c.id,
            title=c.title,
            description=c.description,
            workload=c.workload,
        )
        for c in courses
    ]

    return ApiResponse(
        success=True,
        message="User courses retrieved successfully",
        data=UserCoursesResponse(user=user_response, courses=course_responses),
    )
