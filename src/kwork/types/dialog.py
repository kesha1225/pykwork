from pydantic import BaseModel


class LastMessage(BaseModel):
    unread: bool = None
    fromUsername: str = None
    fromUserId: int = None
    type: str = None
    time: int = None
    message: str = None


class Dialog(BaseModel):
    unread_count: int = None
    last_message: str = None  # last_message text
    time: int = None
    user_id: int = None
    username: str = None
    profilepicture: str = None
    link: str = None
    status: str = None
    blocked_by_user: bool = None
    allowedDialog: bool = None
    lastMessage: LastMessage = None  # object of last_message
    has_active_order: bool = None
    archived: bool = None
    isStarred: bool = None
