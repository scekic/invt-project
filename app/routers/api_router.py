from fastapi import APIRouter

from app.routers import faq
from app.settings import settings

api_router = APIRouter(prefix=settings.API_V1_STR)

api_router.include_router(faq.router)
