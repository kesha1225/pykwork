from typing import List, Optional

from pydantic.v1 import BaseModel

from kwork.types.achievement import Achievement
from kwork.types.kwork_object import KworkObject
from kwork.types.review import Review


class User(BaseModel):
    id: str = None
    username: str = None
    status: str = None
    fullname: str = None
    profilepicture: str = None
    description: str = None
    slogan: str = None
    location: str = None
    rating: float = None
    rating_count: int = None
    level_description: str = None
    good_reviews: int = None
    bad_reviews: int = None
    online: bool = None
    live_date: int = None
    cover: str = None
    custom_request_min_budget: int = None
    is_allow_custom_request: int = None
    order_done_persent: int = None
    order_done_intime_persent: int = None
    order_done_repeat_persent: int = None
    timezoneId: int = None
    blocked_by_user: bool = None
    allowedDialog: bool = None
    addtime: int = None
    achievments_list: List[Achievement] = None
    completed_orders_count: int
    specialization: Optional[str] = None
    profession: Optional[str] = None
    kworks_count: int
    kworks: List[KworkObject]
    portfolio_list: Optional[str] = None
    reviews: Optional[List[Review]] = None
