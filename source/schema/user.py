from kwork.schema.achievement import Achievement
from kwork.schema.kwork_object import KworkObject
from kwork.schema.portfolio import PortfolioItem
from kwork.schema.review import Review
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int | None = None
    username: str | None = None
    status: str | None = None
    fullname: str | None = None
    profilepicture: str | None = None
    description: str | None = None
    slogan: str | None = None
    location: str | None = None
    rating: float | None = None
    rating_count: int | None = None
    level_description: str | None = None
    good_reviews: int | None = None
    bad_reviews: int | None = None
    online: bool | None = None
    live_date: int | None = None
    cover: str | None = None
    custom_request_min_budget: int | None = None
    is_allow_custom_request: int | None = None
    order_done_persent: int | None = None
    order_done_intime_persent: int | None = None
    order_done_repeat_persent: int | None = None
    timezone_id: int | None = Field(None, alias="timezoneId")
    blocked_by_user: bool | None = None
    allowed_dialog: bool | None = Field(None, alias="allowedDialog")
    addtime: int | None = None
    achievments_list: list[Achievement] | None = None
    completed_orders_count: int | None = None
    specialization: str | None = None
    profession: str | None = None
    kworks_count: int | None = None
    kworks: list[KworkObject] | None = None
    portfolio_list: list[PortfolioItem] | None = None
    reviews: list[Review] | None = None
