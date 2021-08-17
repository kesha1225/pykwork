from pydantic import BaseModel
import typing
import asyncio


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
    type: typing.Optional[str] = None
    status: str = None
    created_order_id: typing.Optional[str] = None
    forwarded: bool = None
    updated_at: typing.Optional[int] = None
    message_page: int = None


class Message:
    def __init__(
        self,
        api,
        from_id: int,
        text: str,
        to_user_id: int,
        inbox_id: int,
        title: str,
        last_message: dict,
    ):
        self.api = api
        self.from_id = from_id
        self.text = text
        self.to_user_id = to_user_id
        self.inbox_id = inbox_id
        self.title = title
        self.last_message = last_message

    async def answer_simulation(self, text: str):
        """
        realistic answer with typing simulation and waiting
        :param text:
        :return:
        """
        await asyncio.sleep(2)
        await self.api.set_typing(self.from_id)
        await asyncio.sleep(2)
        await self.api.send_message(self.from_id, text=text)

    async def fast_answer(self, text: str):
        await self.api.send_message(self.from_id, text=text)
