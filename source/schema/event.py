from enum import StrEnum
from typing import Any

from pydantic import BaseModel


class BaseEvent(BaseModel):
    event: str | None = None
    data: dict[str, Any] | None = None


class EventType(StrEnum):
    IS_TYPING = "is_typing"
    NOTIFY = "notify"
    NEW_MESSAGE = "new_inbox"
    POP_UP_NOTIFY = "pop_up_notify"
    MESSAGE_DELETE = "inbox_message_delete"
    REMOVE_POP_UP_NOTIFY = "remove_pop_up_notify"
    DIALOG_UPDATE = "dialog_updated"


class Notify(StrEnum):
    NEW_MESSAGE = "new_message"
