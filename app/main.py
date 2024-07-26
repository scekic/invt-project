from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app import __version__
from app.db import AsyncSessionFactory
from app.routers.api_router import api_router
from app.services.utils import UtilsService
from app.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncSessionFactory() as session:
        await UtilsService.load_csv_data(session)
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=__version__,
    lifespan=lifespan
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
