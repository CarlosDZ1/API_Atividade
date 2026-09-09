"""Main FastAPI application entry point."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import APP_TITLE, APP_DESCRIPTION, APP_VERSION
from app.infrastructure.database.session import engine, Base
from app.presentation.middleware.error_handler import register_error_handlers
from app.presentation.controllers.user_controller import router as user_router
from app.presentation.controllers.course_controller import router as course_router
from app.presentation.controllers.enrollment_controller import router as enrollment_router
from app.presentation.schemas.common import ApiResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager: creates database tables on startup."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register standardized error handlers
register_error_handlers(app)

# Include API Routers
app.include_router(user_router)
app.include_router(course_router)
app.include_router(enrollment_router)


@app.get(
    "/",
    response_model=ApiResponse[dict],
    summary="Root health check and welcome endpoint",
    tags=["Health"],
)
def root():
    return ApiResponse(
        success=True,
        message="Welcome to StudyManager API! Check /docs for interactive Swagger documentation.",
        data={
            "service": APP_TITLE,
            "version": APP_VERSION,
            "docs": "/docs",
        },
    )
