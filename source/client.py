from typing import Any

from kwork.api import KworkAPI
from kwork.schema import (
    Actor,
    Connects,
    DialogMessage,
    InboxMessage,
    ParentCategory,
    User,
    WantWorker,
)


class KworkClient(KworkAPI):
    async def get_me(self) -> Actor:
        data = await self.request("post", "actor", use_token=True)
        return Actor(**data["response"])

    async def get_user(self, user_id: int) -> User:
        data = await self.request("post", "user", id=user_id)
        return User(**data["response"])

    async def set_typing(self, recipient_id: int) -> dict[str, Any]:
        return await self.request(
            "post",
            "typing",
            use_token=True,
            recipientId=recipient_id,
        )

    async def set_offline(self) -> dict[str, Any]:
        return await self.request("post", "offline", use_token=True)

    async def get_channel(self) -> str:
        data = await self.request("post", "getChannel", use_token=True)
        return data["response"]["channel"]

    async def send_message(self, user_id: int, text: str) -> dict[str, Any]:
        return await self.request_with_body(
            "inboxCreate",
            use_token=True,
            body={"text": text},
            user_id=user_id,
        )

    async def delete_message(self, message_id: int) -> dict[str, Any]:
        return await self.request(
            "post",
            "inboxDelete",
            use_token=True,
            id=message_id,
        )

    async def get_dialogs_page(
        self,
        page: int = 1,
        excluded_ids: str | None = None,
    ) -> list[DialogMessage]:
        data = await self.request(
            "post",
            "dialogs",
            use_token=True,
            page=page,
            excludedIds=excluded_ids,
        )
        response = data.get("response") or []
        return [DialogMessage(**d) for d in response]

    async def get_all_dialogs(self) -> list[DialogMessage]:
        dialogs: list[DialogMessage] = []
        page = 1

        while True:
            page_dialogs = await self.get_dialogs_page(page)
            if not page_dialogs:
                break
            dialogs.extend(page_dialogs)
            page += 1

        return dialogs

    async def get_dialog_with_user(self, username: str) -> list[InboxMessage]:
        messages: list[InboxMessage] = []
        page = 1

        while True:
            data = await self.request(
                "post",
                "inboxes",
                use_token=True,
                username=username,
                page=page,
            )

            response = data.get("response")
            if not response:
                break

            messages.extend(InboxMessage(**m) for m in response)

            paging = data.get("paging", {})
            if page >= paging.get("pages", page):
                break
            page += 1

        return messages

    async def get_worker_orders(self) -> dict[str, Any]:
        return await self.request(
            "post",
            "workerOrders",
            use_token=True,
            filter="all",
        )

    async def get_payer_orders(self) -> dict[str, Any]:
        return await self.request(
            "post",
            "payerOrders",
            use_token=True,
            filter="all",
        )

    async def get_notifications(self) -> dict[str, Any]:
        return await self.request("post", "notifications", use_token=True)

    async def get_categories(self) -> list[ParentCategory]:
        data = await self.request("post", "categories")
        return [ParentCategory(**c) for c in data["response"]]

    async def get_connects(self) -> Connects:
        data = await self.request(
            "post",
            "projects",
            use_token=True,
            categories="",
        )
        return Connects(**data["connects"])

    async def get_projects(
        self,
        categories_ids: list[int | str],
        price_from: int | None = None,
        price_to: int | None = None,
        hiring_from: int | None = None,
        kworks_filter_from: int | None = None,
        kworks_filter_to: int | None = None,
        page: int | None = None,
        query: str | None = None,
    ) -> list[WantWorker]:
        """
        Получить список проектов.

        categories_ids: ID рубрик через запятую или 'all' для всех рубрик.
            Пустой список — выборка по любимым рубрикам.
        price_from: Бюджет от (включительно)
        price_to: Бюджет до (включительно)
        hiring_from: Процент найма от
        kworks_filter_from: Количество предложений от (не включительно)
        kworks_filter_to: Количество предложений до (включительно)
        page: Страница выдачи
        query: Поисковая строка
        """
        categories_str = ",".join(str(c) for c in categories_ids)

        data = await self.request(
            "post",
            "projects",
            use_token=True,
            categories=categories_str,
            price_from=price_from,
            price_to=price_to,
            hiring_from=hiring_from,
            kworks_filter_from=kworks_filter_from,
            kworks_filter_to=kworks_filter_to,
            page=page,
            query=query,
        )
        return [WantWorker(**p) for p in data["response"]]
