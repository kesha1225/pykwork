import json
import logging
import asyncio
import urllib.parse
import collections
from typing import Optional, Union

import websockets
import aiohttp

from .types import Message, Actor, EventType, BaseEvent, Notify
from .types.all import *
from kwork.exceptions import KworkException, KworkBotException

logger = logging.getLogger(__name__)
Handler = collections.namedtuple(
    "Handler", ["func", "text", "on_start", "text_contains"]
)


class Kwork:
    def __init__(
        self,
        login: str,
        password: str,
        proxy: typing.Optional[str] = None,
        phone_last: typing.Optional[str] = None,
    ):
        connector: typing.Optional[aiohttp.BaseConnector] = None

        if proxy is not None:
            try:
                from aiohttp_socks import ProxyConnector
            except ImportError:
                raise ImportError(
                    "You have to install aiohttp_socks for using"
                    " proxy, make it by pip install aiohttp_socks"
                )
            connector = ProxyConnector.from_url(proxy)

        self.session = aiohttp.ClientSession(connector=connector)
        self.host = "https://api.kwork.ru/{}"
        self.login = login
        self.password = password
        self._token: typing.Optional[str] = None
        self.phone_last = phone_last

    @property
    async def token(self) -> str:
        if self._token is None:
            self._token = await self.get_token()
        return self._token

    async def api_request(
        self, method: str, api_method: str, **params
    ) -> typing.Union[dict, typing.NoReturn]:
        params = {k: v for k, v in params.items() if v is not None}
        logging.debug(
            f"making {method} request on /{api_method} with params - {params}"
        )
        async with self.session.request(
            method=method,
            url=self.host.format(api_method),
            headers={"Authorization": "Basic bW9iaWxlX2FwaTpxRnZmUmw3dw=="},
            params=params,
        ) as resp:
            if resp.content_type != "application/json":
                error_text: str = await resp.text()
                raise KworkException(error_text)
            json_response: dict = await resp.json()
            if not json_response["success"]:
                raise KworkException(json_response["error"])
            logging.debug(f"result of request on /{api_method} - {json_response}")
            return json_response

    async def close(self) -> None:
        await self.session.close()

    async def get_token(self) -> str:
        resp: dict = await self.api_request(
            method="post",
            api_method="signIn",
            login=self.login,
            password=self.password,
            phone_last=self.phone_last,
        )
        return resp["response"]["token"]

    async def get_me(self) -> Actor:
        actor = await self.api_request(
            method="post", api_method="actor", token=await self.token
        )
        return Actor(**actor["response"])

    async def get_user(self, user_id: int) -> User:
        """
        :param user_id: you can find it in dialogs
        :return:
        """
        user = await self.api_request(
            method="post", api_method="user", id=user_id, token=await self.token
        )
        return User(**user["response"])

    async def set_typing(self, recipient_id: int) -> dict:
        resp = await self.api_request(
            method="post",
            api_method="typing",
            recipientId=recipient_id,
            token=await self.token,
        )
        return resp

    async def get_all_dialogs(self) -> typing.List[DialogMessage]:
        page = 1
        dialogs: typing.List[DialogMessage] = []

        while True:
            dialogs_page = await self.api_request(
                method="post",
                api_method="dialogs",
                filter="all",
                page=page,
                token=await self.token,
            )
            if not dialogs_page["response"]:
                break

            for dialog in dialogs_page["response"]:
                dialogs.append(DialogMessage(**dialog))
            page += 1

        return dialogs

    async def set_offline(self) -> dict:
        return await self.api_request(
            method="post", api_method="offline", token=await self.token
        )

    async def get_dialog_with_user(self, user_name: str) -> typing.List[InboxMessage]:
        page = 1
        dialog: typing.List[InboxMessage] = []

        while True:
            messages_dict: dict = await self.api_request(
                method="post",
                api_method="inboxes",
                username=user_name,
                page=page,
                token=await self.token,
            )
            if not messages_dict.get("response"):
                break
            for message in messages_dict["response"]:
                dialog.append(InboxMessage(**message))

            if page == messages_dict["paging"]["pages"]:
                break
            page += 1

        return dialog

    async def get_worker_orders(self) -> dict:
        return await self.api_request(
            method="post",
            api_method="workerOrders",
            filter="all",
            token=await self.token,
        )

    async def get_payer_orders(self) -> dict:
        return await self.api_request(
            method="post",
            api_method="payerOrders",
            filter="all",
            token=await self.token,
        )

    async def get_notifications(self) -> dict:
        return await self.api_request(
            method="post",
            api_method="notifications",
            token=await self.token,
        )

    async def get_categories(self) -> typing.List[Category]:
        raw_categories = await self.api_request(
            method="post",
            api_method="categories",
            type="1",
            token=await self.token,
        )
        categories = []
        for dict_category in raw_categories["response"]:
            category = Category(**dict_category)
            categories.append(category)
        return categories

    async def get_connects(self) -> Connects:
        raw_projects = await self.api_request(
            method="post",
            api_method="projects",
            categories="",
            token=await self.token,
        )
        return Connects(**raw_projects["connects"])

    async def get_projects(
        self,
        categories_ids: typing.List[Union[int, str]],
        price_from: Optional[int] = None,
        price_to: Optional[int] = None,
        hiring_from: Optional[int] = None,
        kworks_filter_from: Optional[int] = None,
        kworks_filter_to: Optional[int] = None,
        page: Optional[int] = None,
        query: Optional[str] = None,
    ) -> typing.List[WantWorker]:
        """
        categories_ids - Список ID рубрик через запятую, либо 'all' - для выборки по всем рубрикам.
         С пустым значением делает выборку по любимым рубрикам.
        price_from - Бюджет от (включительно)
        price_to - Бюджет до (включительно)
        hiring_from - Процент найма от
        kworks_filter_from - Количество предложений от (не включительно)
        kworks_filter_to - Количество предложений до (включительно)
        page - Страница выдачи
        query - Поисковая строка
        """

        raw_projects = await self.api_request(
            method="post",
            api_method="projects",
            categories=",".join(str(category) for category in categories_ids),
            price_from=price_from,
            price_to=price_to,
            hiring_from=hiring_from,
            kworks_filter_from=kworks_filter_from,
            kworks_filter_to=kworks_filter_to,
            page=page,
            query=query,
            token=await self.token,
        )
        projects = []
        for dict_project in raw_projects["response"]:
            project = WantWorker(**dict_project)
            projects.append(project)
        return projects

    async def _get_channel(self) -> str:
        channel = await self.api_request(
            method="post", api_method="getChannel", token=await self.token
        )
        return channel["response"]["channel"]

    async def send_message(self, user_id: int, text: str) -> dict:  # noqa
        logging.debug(f"Sending message for {user_id} with text - {text}")
        resp = await self.session.post(
            f"{self.host.format('inboxCreate')}"
            f"?user_id={user_id}"
            f"&text={urllib.parse.quote(text)}&token={await self.token}",
            headers={"Authorization": "Basic bW9iaWxlX2FwaTpxRnZmUmw3dw=="},
        )
        json_resp = await resp.json()
        logging.debug(f"result of sending - {json_resp}")
        return json_resp

    async def delete_message(self, message_id) -> dict:
        return await self.api_request(
            method="post",
            api_method="inboxDelete",
            id=message_id,
            token=await self.token,
        )


class KworkBot(Kwork):
    def __init__(self, login: str, password: str, proxy: str = None):
        super().__init__(login, password, proxy)
        self._handlers: typing.List[Handler] = []

    async def listen_messages(self):
        logger.info("Starting listen messages")
        while True:
            try:
                channel = await self._get_channel()
                uri = f"wss://notice.kwork.ru/ws/public/{channel}"
                async with websockets.connect(uri) as websocket:
                    try:
                        data = await websocket.recv()
                    except websockets.exceptions.ConnectionClosedError as e:
                        logging.debug(f"Get {e}, reboot socket...")
                        continue

                    logging.debug(f"Get updates from websocket - {data}")

                    json_event = json.loads(data)
                    json_event_data = json.loads(json_event["text"])

                    event: BaseEvent = BaseEvent(**json_event_data)
                    if event.event in [EventType.IS_TYPING]:
                        continue

                    if event.event == EventType.NEW_MESSAGE:
                        message: Message = Message(
                            api=self,
                            from_id=event.data["from"],
                            text=event.data["inboxMessage"],
                            to_user_id=event.data["to_user_id"],
                            inbox_id=event.data["inbox_id"],
                            title=event.data["title"],
                            last_message=event.data["lastMessage"],
                        )
                        yield message
                    elif (
                        event.event == EventType.NOTIFY
                        and event.data.get(Notify.NEW_MESSAGE) is not None
                    ):
                        if event.data.get("dialog_data") is None:
                            dialogs_page = await self.api_request(
                                method="post",
                                api_method="dialogs",
                                filter="all",
                                page=1,
                                token=await self.token,
                            )
                            last_dialog = DialogMessage(**dialogs_page["response"][0])

                            from_id, text, to_user_id, inbox_id = (
                                last_dialog.user_id,
                                last_dialog.last_message,
                                None,
                                None,
                            )
                        else:
                            # TODO: вынести логику
                            message_raw: InboxMessage = (
                                await self.get_dialog_with_user(
                                    event.data["dialog_data"][0]["login"]
                                )
                            )[0]

                            from_id, text, to_user_id, inbox_id = (
                                message_raw.from_id,
                                message_raw.message,
                                message_raw.to_id,
                                message_raw.message_id,
                            )
                        message: Message = Message(
                            api=self,
                            from_id=from_id,
                            text=text,
                            to_user_id=to_user_id,
                            inbox_id=inbox_id,
                        )
                        yield message

                    elif event.event == EventType.POP_UP_NOTIFY:
                        message_raw: InboxMessage = (
                            await self.get_dialog_with_user(
                                event.data["pop_up_notify"]["data"]["username"]
                            )
                        )[0]
                        message: Message = Message(
                            api=self,
                            from_id=message_raw.from_id,
                            text=message_raw.message,
                            to_user_id=message_raw.to_id,
                            inbox_id=message_raw.message_id,
                        )
                        yield message
            except KworkException as e:
                logging.error(f"Get error in polling - {e}, restarting")
                await asyncio.sleep(10)

    @staticmethod
    def _dispatch_text_contains(text, message_text) -> bool:
        lower_text = [word.lower() for word in message_text.split()]
        for word in lower_text:
            if text == word.strip("...").strip("!").strip(".").strip("?").strip("-"):
                return True
        return False

    async def _dispatch_message(
        self, message: Message, handler: Handler
    ) -> typing.Optional[typing.Callable]:
        if not any([handler.on_start, handler.text, handler.text_contains]):
            return handler.func

        if handler.on_start:
            from_username = (await self.get_all_dialogs())[0].username
            current_dialog = await self.get_dialog_with_user(from_username)
            if len(current_dialog) == 1:
                return handler.func
        elif (
            handler is not None
            and handler.text is not None
            and handler.text.lower() == message.text.lower()
        ):
            return handler.func
        elif handler.text_contains is not None and self._dispatch_text_contains(
            handler.text_contains, message.text
        ):
            return handler.func
        return None

    def message_handler(
        self, text: str = None, on_start: bool = False, text_contains: str = None
    ):
        """
        :param text: answer on exact match of message
        :param on_start: answer only on fist message in dialog
        :param text_contains: answer if message contains this text
        :return:
        """

        def decorator(func: typing.Callable) -> typing.Callable:
            handler = Handler(func, text, on_start, text_contains)
            self._handlers.append(handler)
            return func

        return decorator

    async def run_bot(self):
        if not self._handlers:
            raise KworkBotException("You have to create handler")
        logging.info("Bot is running!")
        async for message in self.listen_messages():
            for handler in self._handlers:
                handler_func = await self._dispatch_message(message, handler)
                logger.debug(f"Found handler - {handler_func}")
                if handler_func is not None:
                    await handler_func(message)
