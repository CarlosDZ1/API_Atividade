"""Pydantic schemas for Enrollment request and response validation."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class EnrollmentCreate(BaseModel):
    """Schema for enrollment creation payload."""

    user_id: int = Field(..., gt=0, description="ID of the user to enroll")
    course_id: int = Field(..., gt=0, description="ID of the course to enroll into")


class EnrollmentResponse(BaseModel):
    """Schema for enrollment data output."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    course_id: int
    enrolled_at: Optional[datetime] = None
