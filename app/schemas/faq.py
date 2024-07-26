from pydantic import BaseModel, ConfigDict


class FAQBase(BaseModel):
    question: str
    complimentary: str | None
    answer: str
    language: str | None
    url: str | None
    category: str | None
    keywords: str | None
    model_config = ConfigDict(from_attributes=True)


class FAQIn(FAQBase):
    pass


class FAQOut(FAQBase):
    id: int
    embedding: list[float] | None
