"""Custom application domain exceptions."""

class DomainException(Exception):
    """Base exception for all domain and application errors."""

    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class EntityNotFoundException(DomainException):
    """Raised when a requested entity does not exist."""

    def __init__(self, message: str):
        super().__init__(message=message, status_code=404)


class DuplicateEntityException(DomainException):
    """Raised when a unique constraint or duplication rule is violated."""

    def __init__(self, message: str):
        super().__init__(message=message, status_code=409)


class ValidationException(DomainException):
    """Raised when domain-level business validation fails."""

    def __init__(self, message: str):
        super().__init__(message=message, status_code=422)
