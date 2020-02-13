from pydantic import BaseModel


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
