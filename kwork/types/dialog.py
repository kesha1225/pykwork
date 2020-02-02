from pydantic import BaseModel


class LastMessage(BaseModel):
    unread: bool
    fromUsername: str
    fromUserId: int
    type: str
    time: int
    message: str


class Dialog(BaseModel):
    unread_count: int
    last_message: str  # last_message text
    time: int
    user_id: int
    username: str
    profilepicture: str
    link: str
    status: str
    blocked_by_user: bool
    allowedDialog: bool
    lastMessage: LastMessage  # object of last_message
    has_active_order: bool
    archived: bool
    isStarred: bool
