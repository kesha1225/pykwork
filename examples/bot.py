import asyncio

from kwork import KworkBot
from kwork.schema import Message

bot = KworkBot(login="login", password="password")


@bot.message_handler(on_start=True)
async def handle_first_message(message: Message) -> None:
    await message.answer_simulation("Здравствуйте! Опишите задачу подробнее.")


@bot.message_handler(text_contains="бот")
async def handle_bot_keyword(message: Message) -> None:
    await message.answer_simulation("Вам нужен бот? Могу помочь!")


@bot.message_handler(text="привет")
async def handle_hello(message: Message) -> None:
    await message.answer_simulation("И вам привет!")


@bot.message_handler()
async def handle_fallback(message: Message) -> None:
    await message.fast_answer("Спасибо! Отвечу в ближайшее время.")


if __name__ == "__main__":
    asyncio.run(bot.run())
