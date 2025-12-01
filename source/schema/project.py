from kwork.schema.achievement import Achievement
from pydantic import BaseModel


class Project(BaseModel):
    """Проект пользователя."""

    id: int | None = None
    user_id: int | None = None
    username: str | None = None
    profile_picture: str | None = None
    price: int | None = None
    title: str | None = None
    description: str | None = None
    offers: int | None = None
    time_left: int | None = None
    parent_category_id: int | None = None
    category_id: int | None = None
    date_confirm: int | None = None
    achievements_list: list[Achievement] | None = None


class WantWorker(BaseModel):
    """Запрос на исполнителя (проект биржи)."""

    id: int | None = None
    status: str | None = None
    user_id: int | None = None
    username: str | None = None
    profile_picture: str | None = None
    price: int | None = None
    title: str | None = None
    description: str | None = None
    offers: int | None = None
    time_left: int | None = None
    parent_category_id: int | None = None
    category_id: int | None = None
    date_confirm: int | None = None
    category_base_price: int | None = None
    user_projects_count: int | None = None
    user_hired_percent: int | None = None
    user_active_projects_count: int | None = None
    achievements_list: list[Achievement] | None = None
    is_viewed: bool | None = None
    already_work: int | None = None
    allow_higher_price: bool | None = None
    possible_price_limit: int | None = None
    user_need_portfolio: int | None = None
    user_need_portfolio_rubric_name: str | None = None
