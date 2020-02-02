from pydantic import BaseModel
import typing
import asyncio


class MessageModel(BaseModel):
    message_id: int
    to_id: int
    to_username: str
    to_live_date: int
    from_id: int
    from_username: str
    from_live_date: int
    from_profilepicture: str
    message: str
    time: int
    unread: bool
    type: typing.Optional[str]
    status: str
    created_order_id: typing.Optional[str]
    forwarded: bool
    updated_at: typing.Optional[int]
    message_page: int


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
