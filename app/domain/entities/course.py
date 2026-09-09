"""Course domain entity."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class CourseEntity:
    """Pure domain entity representing a Course."""

    id: Optional[int]
    title: str
    description: Optional[str]
    workload: int

    def validate(self) -> None:
        """Domain validations for Course."""
        if not self.title or not self.title.strip():
            raise ValueError("Course title must not be empty.")
        if self.workload <= 0:
            raise ValueError("Workload must be greater than 0 hours.")
