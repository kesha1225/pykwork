import asyncio
import logging
from collections.abc import AsyncIterator, Callable
from typing import Any, NamedTuple

import websockets
from kwork.client import KworkClient
from kwork.event_parser import EventParser
from kwork.exceptions import KworkBotException, KworkException
from kwork.schema import Message

logger = logging.getLogger(__name__)

WEBSOCKET_URI = "wss://notice.kwork.ru/ws/public/{}"
RECONNECT_DELAY = 10


class Handler(NamedTuple):
    func: Callable[..., Any]
    text: str | None
    on_start: bool
    text_contains: str | None


class KworkBot(KworkClient):
    def __init__(
        self,
        login: str,
        password: str,
        proxy: str | None = None,
        phone_last: str | None = None,
    ) -> None:
        super().__init__(login, password, proxy, phone_last)
        self._handlers: list[Handler] = []
        self._event_parser = EventParser(self)

    def message_handler(
        self,
        text: str | None = None,
        on_start: bool = False,
        text_contains: str | None = None,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """
        Декоратор для регистрации обработчика сообщений.

        text: Ответить на точное совпадение текста сообщения
        on_start: Ответить только на первое сообщение в диалоге
        text_contains: Ответить если сообщение содержит это слово
        """

        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            handler = Handler(func, text, on_start, text_contains)
            self._handlers.append(handler)
            return func

        return decorator

    async def run(self) -> None:
        if not self._handlers:
            raise KworkBotException("No handlers registered. Add at least one handler.")

        logger.info("Bot is running!")

        async for message in self._listen_messages():
            await self._process_message(message)

    async def _listen_messages(self) -> AsyncIterator[Message]:
        logger.info("Starting message listener")

        while True:
            try:
                async for message in self._websocket_loop():
                    yield message
            except KworkException as e:
                logger.exception("Error in listener: %s. Restarting...", e)
                await asyncio.sleep(RECONNECT_DELAY)

    async def _websocket_loop(self) -> AsyncIterator[Message]:
        channel = await self.get_channel()
        uri = WEBSOCKET_URI.format(channel)

        async with websockets.connect(uri) as ws:
            while True:
                message = await self._receive_message(ws)
                if message is not None:
                    yield message

    async def _receive_message(
        self,
        ws: websockets.ClientConnection,
    ) -> Message | None:
        try:
            raw_data = await ws.recv()
        except websockets.exceptions.ConnectionClosedError as e:
            logger.debug("Connection closed: %s. Reconnecting...", e)
            raise KworkException("WebSocket connection closed") from e

        logger.debug("Received: %s", raw_data)

        event = self._event_parser.parse_raw_event(str(raw_data))
        if event is None or self._event_parser.should_skip_event(event):
            return None

        return await self._event_parser.extract_message(event)

    async def _process_message(self, message: Message) -> None:
        for handler in self._handlers:
            if await self._should_handle(message, handler):
                logger.debug("Dispatching to handler: %s", handler.func.__name__)
                await handler.func(message)
                break

    async def _should_handle(self, message: Message, handler: Handler) -> bool:
        if not any([handler.on_start, handler.text, handler.text_contains]):
            return True

        if handler.on_start:
            return await self._check_is_first_message(message)

        if handler.text is not None:
            return handler.text.lower() == message.text.lower()

        if handler.text_contains is not None:
            return self._text_contains_word(handler.text_contains, message.text)

        return False

    async def _check_is_first_message(self, message: Message) -> bool:
        dialogs = await self.get_all_dialogs()
        if not dialogs:
            return False

        username = dialogs[0].username
        if not username:
            return False

        current_dialog = await self.get_dialog_with_user(username)
        return len(current_dialog) == 1

    @staticmethod
    def _text_contains_word(word: str, text: str) -> bool:
        punctuation = ".,!?;:\"'()-…"
        words = text.lower().split()
        return any(word.lower() == w.strip(punctuation) for w in words)
