from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    status: str
    fullname: str
    profilepicture: str
    description: str
    slogan: str
    location: str
    rating: float
    rating_count: int
    level_description: str
    good_reviews: int
    bad_reviews: int
    online: bool
    live_date: int
    cover: str
    custom_request_min_budget: int
    is_allow_custom_request: int
    order_done_persent: int
    order_done_intime_persent: int
    order_done_repeat_persent: int
    timezoneId: int
    blocked_by_user: bool
    allowedDialog: bool
    addtime: int
