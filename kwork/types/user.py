from pydantic import BaseModel


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
