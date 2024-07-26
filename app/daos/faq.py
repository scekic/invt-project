from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.daos.base import BaseDao
from app.models.faq import FAQ


class FAQDao(BaseDao):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def create(self, faq_data) -> FAQ:
        _faq = FAQ(**faq_data)
        self.session.add(_faq)
        await self.session.commit()
        await self.session.refresh(_faq)
        return _faq

    async def get_by_id(self, faq_id: int) -> FAQ | None:
        statement = select(FAQ).where(FAQ.id == faq_id)
        return await self.session.scalar(statement=statement)

    async def get_by_question(self, question) -> FAQ | None:
        statement = select(FAQ).where(FAQ.question == question)
        return await self.session.scalar(statement=statement)

    async def get_all(self, page: int = 1, page_size: int = 10) -> list[FAQ]:
        offset = (page - 1) * page_size
        statement = (
            select(FAQ)
            .order_by(FAQ.id)
            .offset(offset)
            .limit(page_size)
        )
        result = await self.session.execute(statement=statement)
        return result.scalars().all()
