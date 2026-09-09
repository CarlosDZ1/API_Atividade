"""Course presentation controller/router."""
from typing import List
from fastapi import APIRouter, Depends, status
from app.presentation.schemas.common import ApiResponse
from app.presentation.schemas.course_schema import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
)
from app.presentation.dependencies import (
    get_create_course_use_case,
    get_list_courses_use_case,
    get_get_course_use_case,
    get_update_course_use_case,
    get_delete_course_use_case,
)
from app.use_cases.course.create_course import CreateCourseUseCase
from app.use_cases.course.list_courses import ListCoursesUseCase
from app.use_cases.course.get_course import GetCourseUseCase
from app.use_cases.course.update_course import UpdateCourseUseCase
from app.use_cases.course.delete_course import DeleteCourseUseCase

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ApiResponse[CourseResponse],
    summary="Create a new course",
)
def create_course(
    payload: CourseCreate,
    use_case: CreateCourseUseCase = Depends(get_create_course_use_case),
):
    created_course = use_case.execute(
        title=payload.title,
        description=payload.description,
        workload=payload.workload,
    )
    return ApiResponse(
        success=True,
        message="Course created successfully",
        data=CourseResponse(
            id=created_course.id,
            title=created_course.title,
            description=created_course.description,
            workload=created_course.workload,
        ),
    )


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[List[CourseResponse]],
    summary="List all courses",
)
def list_courses(
    use_case: ListCoursesUseCase = Depends(get_list_courses_use_case),
):
    courses = use_case.execute()
    data = [
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
        message="Courses retrieved successfully",
        data=data,
    )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[CourseResponse],
    summary="Get course by ID",
)
def get_course(
    id: int,
    use_case: GetCourseUseCase = Depends(get_get_course_use_case),
):
    course = use_case.execute(course_id=id)
    return ApiResponse(
        success=True,
        message="Course retrieved successfully",
        data=CourseResponse(
            id=course.id,
            title=course.title,
            description=course.description,
            workload=course.workload,
        ),
    )


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[CourseResponse],
    summary="Update course by ID",
)
def update_course(
    id: int,
    payload: CourseUpdate,
    use_case: UpdateCourseUseCase = Depends(get_update_course_use_case),
):
    updated_course = use_case.execute(
        course_id=id,
        title=payload.title,
        description=payload.description,
        workload=payload.workload,
    )
    return ApiResponse(
        success=True,
        message="Course updated successfully",
        data=CourseResponse(
            id=updated_course.id,
            title=updated_course.title,
            description=updated_course.description,
            workload=updated_course.workload,
        ),
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ApiResponse[None],
    summary="Delete course by ID",
)
def delete_course(
    id: int,
    use_case: DeleteCourseUseCase = Depends(get_delete_course_use_case),
):
    use_case.execute(course_id=id)
    return ApiResponse(
        success=True,
        message="Course deleted successfully",
        data=None,
    )
