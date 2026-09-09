"""Common presentation response schemas."""
from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

DataT = TypeVar("DataT")


class ApiResponse(BaseModel, Generic[DataT]):
    """Standardized API response envelope."""

    success: bool
    message: str
    data: Optional[DataT] = None
