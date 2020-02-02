from pydantic import BaseModel


class Actor(BaseModel):
    id: str
    username: str
    status: str
    email: str
    type: str
    verified: bool
    profilepicture: str
    description: str
    slogan: str
    fullname: str
    level_description: str
    cover: str
    good_reviews: int
    bad_reviews: int
    location: str
    rating: float
    rating_count: int
    total_amount: int
    hold_amount: int
    free_amount: int
    inbox_archive_count: int
    unread_dialog_count: int
    notify_unread_count: int
    red_notify: bool
    warning_inbox_count: int
    app_notify_count: int
    unread_messages_count: int
    fullnameEn: str
    descriptionEn: str
    country_id: int
    city_id: int
    timezone_id: int
    addtime: int
    allow_mobile_push: bool
