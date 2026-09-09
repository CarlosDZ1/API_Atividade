"""User domain entity."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class UserEntity:
    """Pure domain entity representing a User."""

    id: Optional[int]
    name: str
    email: str
    created_at: Optional[datetime] = None

    def validate(self) -> None:
        """Domain validations for User."""
        if not self.name or not self.name.strip():
            raise ValueError("User name must not be empty.")
        if not self.email or "@" not in self.email:
            raise ValueError("Invalid email format.")
