import asyncio
import re

from kwork import KworkBot
from kwork.schema import Message

bot = KworkBot(login="login", password="password")

PRICE_KEYWORDS = ["цена", "стоимость", "сколько стоит", "прайс"]
PORTFOLIO_KEYWORDS = ["портфолио", "примеры работ", "примеры"]
DEADLINE_KEYWORDS = ["срок", "сроки", "когда", "как быстро"]


def contains_any(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(kw in text_lower for kw in keywords)


@bot.message_handler(on_start=True)
async def handle_welcome(message: Message) -> None:
    await message.answer_simulation("Здравствуйте! Опишите задачу, и я подготовлю предложение.")


@bot.message_handler(text_contains="бот")
async def handle_bot_request(message: Message) -> None:
    await message.answer_simulation("Вам нужен бот? Для какой платформы и какой функционал?")


@bot.message_handler(text_contains="парсинг")
async def handle_parsing_request(message: Message) -> None:
    await message.answer_simulation("Нужен парсинг? Какой сайт и какие данные собрать?")


@bot.message_handler()
async def handle_default(message: Message) -> None:
    text = message.text.lower()

    if contains_any(text, PRICE_KEYWORDS):
        response = "Стоимость зависит от сложности. Опишите задачу — назову цену."
    elif contains_any(text, PORTFOLIO_KEYWORDS):
        response = "Портфолио: боты, парсеры, автоматизация. Могу показать примеры."
    elif contains_any(text, DEADLINE_KEYWORDS):
        response = "Сроки: простой проект 1-3 дня, сложный до 2 недель."
    elif re.search(r"\bтелеграм|\btg\b|telegram", text):
        response = "Telegram-боты — моя специализация! Какой функционал нужен?"
    else:
        response = "Спасибо за сообщение! Опишите задачу подробнее."

    await message.answer_simulation(response)


if __name__ == "__main__":
    asyncio.run(bot.run())
