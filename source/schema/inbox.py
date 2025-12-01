from typing import Any

from pydantic import BaseModel


class InboxMessage(BaseModel):
    """Входящее сообщение."""

    message_id: int | None = None
    to_id: int | None = None
    to_username: str | None = None
    to_live_date: int | None = None
    from_id: int | None = None
    from_username: str | None = None
    from_live_date: int | None = None
    from_profilepicture: str | None = None
    to_profilepicture: str | None = None
    message: str | None = None
    time: int | None = None
    unread: bool | None = None
    type: str | None = None
    status: str | None = None
    created_order_id: str | None = None
    forwarded: bool | None = None
    updated_at: int | None = None
    warning_type: str | None = None
    countup: int | None = None
    files: list[Any] | None = None
    quote: dict[str, Any] | None = None
    message_page: int | None = None
    custom_request: dict[str, Any] | None = None
    inbox_order: dict[str, Any] | None = None
