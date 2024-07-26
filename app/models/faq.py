from sqlalchemy import Float, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, intpk


class FAQ(Base):
    __tablename__ = "faq"

    id: Mapped[intpk]
    question: Mapped[str] = mapped_column(Text,
                                          unique=True,
                                          index=True,
                                          nullable=False)
    complimentary: Mapped[str | None] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)
    language: Mapped[str | None]
    url: Mapped[str | None]
    category: Mapped[str | None]
    keywords: Mapped[str | None] = mapped_column(Text)
    embedding: Mapped[list[float] | None] = mapped_column(ARRAY(Float))
