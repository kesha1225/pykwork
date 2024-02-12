from typing import List, Optional

from pydantic.v1 import BaseModel, Field

from kwork.types.achievement import Achievement
from kwork.types.kwork_object import KworkObject
from kwork.types.portfolio import PortfolioItem
from kwork.types.review import Review


class Actor(BaseModel):
    id: str = None
    username: str = None
    status: str = None
    email: str = None
    type: str = None
    verified: bool = None
    profile_picture: str = Field(None, alias="profilepicture")
    description: str = None
    slogan: str = None
    fullname: str = None
    level_description: str = None
    cover: str = None
    good_reviews: int = None
    bad_reviews: int = None
    location: str = None
    rating: float = None
    rating_count: int = None
    total_amount: int = None
    hold_amount: int = None
    free_amount: int = None
    currency: str = None
    inbox_archive_count: int = None
    unread_dialog_count: int = None
    notify_unread_count: int = None
    red_notify: bool = None
    warning_inbox_count: int = None
    app_notify_count: int = None
    unread_messages_count: int = None
    fullname_en: Optional[str] = Field(None, alias="fullnameEn")
    description_en: Optional[str] = Field(None, alias="descriptionEn")
    country_id: int = None
    city_id: int = None
    timezone_id: int = None
    addtime: int = None
    allow_mobile_push: bool = None
    is_more_payer: bool = None
    kworks_count: int = None
    favourite_kworks_count: int = None
    hidden_kworks_count: int = None
    specialization: Optional[str] = None
    profession: Optional[str] = None
    kworks_available_at_weekends: bool = None
    achievments_list: List[Achievement] = None
    completed_orders_count: int = None
    kworks: List[KworkObject] = None
    portfolio_list: List[PortfolioItem] = None
    reviews: Optional[List[Review]] = None
    worker_status: str = None
    has_offers: bool = None
    wants_count: int = None
    offers_count: int = None
    archived_wants_count: int = None
    push_notifications_sound_allowed: bool = Field(
        None, alias="pushNotificationsSoundAllowed"
    )
    black_friday_for_sellers: bool = None
