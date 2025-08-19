from __future__ import annotations

import asyncio

from pydantic import BaseModel


class MessageModel(BaseModel):
    message_id: int = None
    to_id: int = None
    to_username: str = None
    to_live_date: int = None
    from_id: int = None
    from_username: str = None
    from_live_date: int = None
    from_profilepicture: str = None
    message: str = None
    time: int = None
    unread: bool = None
    type: str | None = None
    status: str = None
    created_order_id: str | None = None
    forwarded: bool = None
    updated_at: int | None = None
    message_page: int = None


class Message:
    def __init__(
        self,
        api,
        from_id: int,
        text: str,
        to_user_id: int | None = None,
        inbox_id: int | None = None,
        last_message: dict | None = None,
        title: str | None = None,
    ) -> None:
        self.api = api
        self.from_id = from_id
        self.text = text
        self.to_user_id = to_user_id
        self.inbox_id = inbox_id
        self.title = title
        self.last_message = last_message

    async def answer_simulation(self, text: str) -> None:
        """Realistic answer with typing simulation and waiting
        :param text:
        :return:
        """
        await asyncio.sleep(2)
        await self.api.set_typing(self.from_id)
        await asyncio.sleep(2)
        await self.api.send_message(self.from_id, text=text)

    async def fast_answer(self, text: str) -> None:
        await self.api.send_message(self.from_id, text=text)
