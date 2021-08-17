from typing import Optional, List

from pydantic import BaseModel, Field

from kwork.types.achievement import Achievement


class Actor(BaseModel):
    id: str
    username: str
    status: str
    email: str
    type: str
    verified: bool
    profile_picture: str = Field(..., alias="profilepicture")
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
    currency: str
    inbox_archive_count: int
    unread_dialog_count: int
    notify_unread_count: int
    red_notify: bool
    warning_inbox_count: int
    app_notify_count: int
    unread_messages_count: int
    fullname_en: Optional[str] = Field(None, alias="fullnameEn")
    description_en: Optional[str] = Field(None, alias="descriptionEn")
    country_id: int
    city_id: int
    timezone_id: int
    addtime: int
    allow_mobile_push: bool
    is_more_payer: bool
    kworks_count: int
    favourite_kworks_count: int
    hidden_kworks_count: int
    specialization: str
    profession: str
    kworks_available_at_weekends: bool
    achievments_list: List[Achievement]
    completed_orders_count: int
    kworks: List  # TODo
    portfolio_list: Optional[str]
    reviews: List  # TODo
    worker_status: str
    has_offers: bool
    wants_count: int
    offers_count: int
    archived_wants_count: int
    push_notifications_sound_allowed: bool = Field(..., alias="pushNotificationsSoundAllowed")
