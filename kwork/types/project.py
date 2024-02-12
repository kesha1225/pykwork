from typing import List

from pydantic.v1 import BaseModel

from kwork.types.achievement import Achievement


class Project(BaseModel):
    id: int = None
    user_id: int = None
    username: str = None
    profile_picture: str = None
    price: int = None
    title: str = None
    description: str = None
    offers: int = None
    time_left: int = None
    parent_category_id: int = None
    category_id: int = None
    date_confirm: int = None
    category_base_price: int = None
    user_projects_count: int = None
    user_hired_percent: int = None
    achievements_list: List[Achievement] = None
    is_viewed: bool = None
    already_work: int = None
    allow_higher_price: bool = None
    possible_price_limit: int = None
