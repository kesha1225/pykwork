from pydantic import BaseModel


class BaseEvent(BaseModel):
    event: str = None
    data: dict = None


class EventType:
    IS_TYPING = "is_typing"
    NOTIFY = "notify"
    NEW_MESSAGE = "new_inbox"
    POP_UP_NOTIFY = "pop_up_notify"
    MESSAGE_DELETE = "inbox_message_delete"
    REMOVE_POP_UP_NOTIFY = "remove_pop_up_notify"
    DIALOG_UPDATE = "dialog_updated"


class Notify:
    NEW_MESSAGE = "new_message"
