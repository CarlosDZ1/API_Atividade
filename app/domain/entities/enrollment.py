"""Enrollment domain entity."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EnrollmentEntity:
    """Pure domain entity representing an Enrollment."""

    id: Optional[int]
    user_id: int
    course_id: int
    enrolled_at: Optional[datetime] = None

    def validate(self) -> None:
        """Domain validations for Enrollment."""
        if not self.user_id or self.user_id <= 0:
            raise ValueError("Valid user_id is required.")
        if not self.course_id or self.course_id <= 0:
            raise ValueError("Valid course_id is required.")
