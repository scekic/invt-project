# import asyncio
import csv
# import random
# import time

# import openai
# from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from app.daos import faq
from app.schemas.faq import FAQIn
# from app.settings import settings


class UtilsService:
    @staticmethod
    async def load_csv_data(session: AsyncSession):
        with open("app/faq_knowledge_base.csv", mode="r") as file:
            reader = csv.DictReader(file)
            faqs_to_create = []
            # processed_questions = set()

            for row in reader:
                question = row["Article title - Question"]
                _faq = await faq.FAQDao(session).get_by_question(question)
                if not _faq:
                    new_faq_data = FAQIn(
                        question=question,
                        complimentary=row["Article subtitle - Complementary"],
                        answer=row["Article body - Answer"],
                        language=row["Article language"],
                        url=row["Article URL"],
                        category=row["Category"],
                        keywords=row["Keywords"],
                    )
                    faqs_to_create.append(new_faq_data)
                    await faq.FAQDao(session).create(  # remove these lines
                            new_faq_data.model_dump()  # if uncommeting the
                            )                          # rest of the code

            # batch_size = 20
            # for i in range(0, len(faqs_to_create), batch_size):
            #     batch_faqs = faqs_to_create[i: i + batch_size]
            #     batch_texts = [
            #         UtilsService.concatenate_faq_data(faq_data)
            #         for faq_data in batch_faqs
            #     ]

            #     try:
            #         embeddings = await UtilsService.create_embeddings_with_retry(
            #             batch_texts
            #         )
            #     except openai.RateLimitError as e:
            #         if "quota" in str(e):
            #             logger.error("Quota exceeded. Waiting for reset.")
            #             time_to_reset = 60
            #             time.sleep(time_to_reset)
            #             continue

            #     for new_faq_data, embedding in zip(batch_faqs, embeddings):
            #         if new_faq_data.question not in processed_questions:
            #             new_faq_data.embedding = embedding
            #             await faq.FAQDao(session).create(
            #                 new_faq_data.model_dump()
            #                 )
            #             processed_questions.add(new_faq_data.question)

            #     await asyncio.sleep(2)

    # @staticmethod
    # def concatenate_faq_data(faq_data: FAQIn) -> str:
    #     """Concatenate all relevant fields in FAQIn
    #     to form a single string for generating embeddings."""
    #     return f"{
    #         faq_data.question} {
    #         faq_data.complimentary} {
    #         faq_data.answer} {
    #             faq_data.language} {
    #                 faq_data.url} {
    #                     faq_data.category} {
    #                         faq_data.keywords}"

    # @staticmethod
    # async def create_embeddings_with_retry(inputs: list[str]) -> list:
    #     client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

    #     async def create_embeddings(input_texts):
    #         for attempt in range(5):
    #             try:
    #                 response = await client.embeddings.create(
    #                     input=input_texts, model="text-embedding-ada-002"
    #                 )
    #                 return [item["embedding"] for item in response["data"]]
    #             except openai.RateLimitError as e:
    #                 if "quota" in str(e):
    #                     raise e
    #                 if attempt < 4:
    #                     wait_time = (2**attempt) + (random.random() * 0.5)
    #                     await asyncio.sleep(wait_time)
    #                 else:
    #                     raise

    #     return await create_embeddings(inputs)
