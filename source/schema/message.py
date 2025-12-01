import asyncio
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

if TYPE_CHECKING:
    from kwork.client import KworkClient


class MessageModel(BaseModel):
    message_id: int | None = None
    to_id: int | None = None
    to_username: str | None = None
    to_live_date: int | None = None
    from_id: int | None = None
    from_username: str | None = None
    from_live_date: int | None = None
    from_profilepicture: str | None = None
    message: str | None = None
    time: int | None = None
    unread: bool | None = None
    type: str | None = None
    status: str | None = None
    created_order_id: str | None = None
    forwarded: bool | None = None
    updated_at: int | None = None
    message_page: int | None = None


class Message:
    def __init__(
        self,
        api: "KworkClient",
        from_id: int,
        text: str,
        to_user_id: int | None = None,
        inbox_id: int | None = None,
        last_message: dict[str, Any] | None = None,
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
        await asyncio.sleep(2)
        await self.api.set_typing(self.from_id)
        await asyncio.sleep(2)
        await self.api.send_message(self.from_id, text=text)

    async def fast_answer(self, text: str) -> None:
        await self.api.send_message(self.from_id, text=text)
