from kwork.schema.achievement import Achievement
from kwork.schema.kwork_object import KworkObject
from kwork.schema.portfolio import PortfolioItem
from kwork.schema.review import Review
from pydantic import BaseModel, Field


class Actor(BaseModel):
    id: int | None = None
    username: str | None = None
    status: str | None = None
    email: str | None = None
    type: str | None = None
    verified: bool | None = None
    profile_picture: str | None = Field(None, alias="profilepicture")
    description: str | None = None
    slogan: str | None = None
    fullname: str | None = None
    level_description: str | None = None
    cover: str | None = None
    good_reviews: int | None = None
    bad_reviews: int | None = None
    location: str | None = None
    rating: float | None = None
    rating_count: int | None = None
    total_amount: int | None = None
    hold_amount: int | None = None
    free_amount: int | None = None
    currency: str | None = None
    inbox_archive_count: int | None = None
    unread_dialog_count: int | None = None
    notify_unread_count: int | None = None
    red_notify: bool | None = None
    warning_inbox_count: int | None = None
    app_notify_count: int | None = None
    unread_messages_count: int | None = None
    fullname_en: str | None = Field(None, alias="fullnameEn")
    description_en: str | None = Field(None, alias="descriptionEn")
    country_id: int | None = None
    city_id: int | None = None
    timezone_id: int | None = None
    addtime: int | None = None
    allow_mobile_push: bool | None = None
    is_more_payer: bool | None = None
    kworks_count: int | None = None
    favourite_kworks_count: int | None = None
    hidden_kworks_count: int | None = None
    specialization: str | None = None
    profession: str | None = None
    kworks_available_at_weekends: bool | None = None
    achievments_list: list[Achievement] | None = None
    completed_orders_count: int | None = None
    kworks: list[KworkObject] | None = None
    portfolio_list: list[PortfolioItem] | None = None
    reviews: list[Review] | None = None
    worker_status: str | None = None
    has_offers: bool | None = None
    wants_count: int | None = None
    offers_count: int | None = None
    archived_wants_count: int | None = None
    push_notifications_sound_allowed: bool | None = Field(
        None,
        alias="pushNotificationsSoundAllowed",
    )
    black_friday_for_sellers: bool | None = None
