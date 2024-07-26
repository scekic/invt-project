from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from app.daos import faq
from app.schemas.faq import FAQIn, FAQOut
# from app.services.utils import UtilsService


class FAQService:
    @staticmethod
    async def create_faq(faq_data: FAQIn, session: AsyncSession):
        # text_to_embed = UtilsService.concatenate_faq_data(faq_data)
        # embedding = (
        #     await UtilsService.create_embeddings_with_retry(
        #         [text_to_embed]))[0]    # when ucommeting these lines make sure the
        # faq_data.embedding = embedding  # UtilsService is uncommented as well
        new_faq = await faq.FAQDao(session).create(faq_data.model_dump())
        logger.info(f"New FAQ added successfully: {new_faq}!!!")
        return JSONResponse(
            content={"message": "FAQ added successfully"},
            status_code=status.HTTP_201_CREATED,
        )

    @staticmethod
    async def get_all_faqs(
        session: AsyncSession, page: int = 1, page_size: int = 10
    ) -> list[FAQOut]:
        all_faqs = await faq.FAQDao(session).get_all(page=page,
                                                     page_size=page_size)
        return [FAQOut.model_validate(_faq) for _faq in all_faqs]

    @staticmethod
    async def get_faq_by_id(faq_id: int, session: AsyncSession) -> FAQOut:
        _faq = await faq.FAQDao(session).get_by_id(faq_id)
        if not _faq:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="FAQ with the given id does not exist!!!",
            )
        return FAQOut.model_validate(_faq)
