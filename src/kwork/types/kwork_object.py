from typing import List, Optional

from pydantic import BaseModel, Field


class Cover(BaseModel):
    phone: str = None
    tablet: str = None


class Worker(BaseModel):
    id: int = None
    username: str = None
    fullname: str = None
    profilepicture: str = None
    rating: float = None
    reviews_count: int = None
    rating_count: int = None
    is_online: bool = None


class Activity(BaseModel):
    views: int = None
    orders: int = None
    earned: int = None


class KworkObject(BaseModel):
    id: int = None
    category_id: int = None
    category_name: str = None
    status_id: int = None
    status_name: str = None
    title: str = None
    url: str = None
    image_url: str = None
    cover: Cover = None
    price: int = None
    is_price_from: bool = None
    is_from: bool = None
    photo: str = None
    is_best: bool = None
    is_hidden: bool = None
    is_favorite: bool = None
    lang: str = None
    worker: Worker = None
    activity: Activity = None
    edits_list: Optional[list] = None
    profile_sort: int = None
    is_subscription: bool = Field(None, alias="isSubscription")
    badges: List = None  # TODO: что тут
