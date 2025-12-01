from pydantic import BaseModel, Field


class DialogLastMessage(BaseModel):
    """Последнее сообщение в диалоге."""

    unread: bool | None = None
    from_username: str | None = Field(None, alias="fromUsername")
    from_user_id: int | None = Field(None, alias="fromUserId")
    type: str | None = None
    time: int | None = None
    message: str | None = None
    profile_picture: str | None = Field(None, alias="profilePicture")


class DialogMessage(BaseModel):
    """Диалог с пользователем."""

    unread: int | None = None
    unread_count: int | None = None
    last_message: str | None = None
    time: int | None = None
    user_id: int | None = None
    username: str | None = None
    profilepicture: str | None = None
    is_online: bool | None = None
    last_online_time: int | None = Field(None, alias="lastOnlineTime")
    link: str | None = None
    status: str | None = None
    blocked_by_user: bool | None = None
    allowed_dialog: bool | None = Field(None, alias="allowedDialog")
    last_message_obj: DialogLastMessage | None = Field(None, alias="lastMessage")
    has_active_order: bool | None = None
    archived: bool | None = None
    is_starred: bool | None = Field(None, alias="isStarred")
    warning_message_id: int | None = None
    warning_message_time: int | None = None
    countup: int | None = None
    has_answer: bool | None = None
    is_allow_custom_request: bool | None = None
    hidden_at: int | None = None
    disallow_reason: int | None = Field(None, alias="disallowReason")
