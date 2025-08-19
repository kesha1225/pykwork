import asyncio
import logging

from kwork import KworkBot
from kwork.types import Message

logging.basicConfig(level=logging.INFO)

bot = KworkBot(login="login", password="password")


# Можно использовать socks5 прокси
# bot = KworkBot(login="login", password="password", proxy="socks5://64.90.53.198:46088")


@bot.message_handler(on_start=True)
async def simple_handle(message: Message) -> None:
    """Отвечаем только если это первое сообщение от юзера
    :param message:
    :return:
    """
    text = (
        "Здравствуйте, рад что вы обратились именно ко мне,"
        " опишите ваше желание подробнее!"
    )

    # await message.fast_answer(text) быстрый ответ без симуляции
    await message.answer_simulation(text)


@bot.message_handler(text_contains="бот")
async def bot_handler(message: Message) -> None:
    """Отвечаем если текст сообщения содержит слово бот
    :param message:
    :return:
    """
    text = "Вам нужен бот? Можете посмотреть на примеры уже сделанных:..."
    await message.answer_simulation(text)


@bot.message_handler(text="привет")
async def bot_handler(message: Message) -> None:
    """Отвечаем только если текст такой же как параметр text
    :param message:
    :return:
    """
    text = "И вам привет!"
    await message.answer_simulation(text)


async def run() -> None:
    """Запускаем бота
    :return:
    """
    await bot.run_bot()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
