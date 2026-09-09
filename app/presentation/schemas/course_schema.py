"""Pydantic schemas for Course request and response validation."""
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class CourseCreate(BaseModel):
    """Schema for course creation payload."""

    title: str = Field(..., min_length=2, max_length=200, description="Title of the course")
    description: Optional[str] = Field(None, max_length=2000, description="Course description")
    workload: int = Field(..., gt=0, description="Workload in hours (must be greater than 0)")


class CourseUpdate(BaseModel):
    """Schema for course update payload."""

    title: str = Field(..., min_length=2, max_length=200, description="Title of the course")
    description: Optional[str] = Field(None, max_length=2000, description="Course description")
    workload: int = Field(..., gt=0, description="Workload in hours (must be greater than 0)")


class CourseResponse(BaseModel):
    """Schema for course data output."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str] = None
    workload: int
