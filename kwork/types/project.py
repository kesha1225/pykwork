from typing import List

from pydantic import BaseModel

from kwork.types.achievement import Achievement


class Project(BaseModel):
    id: int
    user_id: int
    username: str
    profile_picture: str
    price: int
    title: str
    description: str
    offers: int
    time_left: int
    parent_category_id: int
    category_id: int
    date_confirm: int
    category_base_price: int
    user_projects_count: int
    user_hired_percent: int
    achievements_list: List[Achievement]
    is_viewed: bool
    already_work: int
    allow_higher_price: bool
    possible_price_limit: int
