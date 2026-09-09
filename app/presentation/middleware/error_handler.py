"""Global error handlers to guarantee standardized JSON responses."""
import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.exceptions import DomainException

logger = logging.getLogger("studymanager")


def register_error_handlers(app: FastAPI) -> None:
    """Register custom exception handlers on the FastAPI application."""

    @app.exception_handler(DomainException)
    async def domain_exception_handler(request: Request, exc: DomainException):
        """Handles all business and domain-level exceptions."""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.message,
                "data": None,
            },
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """Handles Starlette/FastAPI HTTP exceptions."""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": str(exc.detail),
                "data": None,
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Handles Pydantic input validation errors with a clean message."""
        error_messages = []
        for error in exc.errors():
            loc = " -> ".join(str(l) for l in error.get("loc", []) if l != "body")
            msg = error.get("msg", "Invalid value")
            if loc:
                error_messages.append(f"Field '{loc}': {msg}")
            else:
                error_messages.append(msg)

        combined_message = "; ".join(error_messages) if error_messages else "Invalid request data."

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "success": False,
                "message": combined_message,
                "data": None,
            },
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Catches any unexpected server errors."""
        logger.exception("Unhandled server exception: %s", exc)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "An unexpected internal server error occurred.",
                "data": None,
            },
        )
