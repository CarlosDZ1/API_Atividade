"""Enrollment presentation controller/router."""
from fastapi import APIRouter, Depends, status
from app.presentation.schemas.common import ApiResponse
from app.presentation.schemas.enrollment_schema import (
    EnrollmentCreate,
    EnrollmentResponse,
)
from app.presentation.dependencies import get_create_enrollment_use_case
from app.use_cases.enrollment.create_enrollment import CreateEnrollmentUseCase

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ApiResponse[EnrollmentResponse],
    summary="Enroll a user in a course",
)
def create_enrollment(
    payload: EnrollmentCreate,
    use_case: CreateEnrollmentUseCase = Depends(get_create_enrollment_use_case),
):
    enrollment = use_case.execute(user_id=payload.user_id, course_id=payload.course_id)
    return ApiResponse(
        success=True,
        message="Enrollment completed successfully",
        data=EnrollmentResponse(
            id=enrollment.id,
            user_id=enrollment.user_id,
            course_id=enrollment.course_id,
            enrolled_at=enrollment.enrolled_at,
        ),
    )
