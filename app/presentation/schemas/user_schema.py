"""Pydantic schemas for User request and response validation."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from app.presentation.schemas.course_schema import CourseResponse


class UserCreate(BaseModel):
    """Schema for user creation payload."""

    name: str = Field(..., min_length=2, max_length=150, description="Full name of the user")
    email: EmailStr = Field(..., description="Unique email address of the user")


class UserUpdate(BaseModel):
    """Schema for user update payload."""

    name: str = Field(..., min_length=2, max_length=150, description="Full name of the user")
    email: EmailStr = Field(..., description="Unique email address of the user")


class UserResponse(BaseModel):
    """Schema for user data output."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    created_at: Optional[datetime] = None


class UserCoursesResponse(BaseModel):
    """Schema for user data combined with their enrolled courses."""

    user: UserResponse
    courses: List[CourseResponse]
