from fastapi import APIRouter, status

from app.db import SessionDep
from app.schemas.faq import FAQIn, FAQOut
from app.services.faq import FAQService

router = APIRouter(tags=["FAQ"], prefix="/faq")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_faq(
    faq_data: FAQIn,
    session: SessionDep,
):
    return await FAQService.create_faq(faq_data, session)


@router.get("/{faq_id}", status_code=status.HTTP_200_OK)
async def get_faq_by_id(
    faq_id: int,
    session: SessionDep,
) -> FAQOut:
    return await FAQService.get_faq_by_id(faq_id, session)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_faqs(
    session: SessionDep, page: int = 1, page_size: int = 10
) -> list[FAQOut]:
    return await FAQService.get_all_faqs(session,
                                         page=page,
                                         page_size=page_size)
