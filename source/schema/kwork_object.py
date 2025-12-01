from typing import Any

from pydantic import BaseModel, Field


class Cover(BaseModel):
    phone: str | None = None
    tablet: str | None = None


class Worker(BaseModel):
    id: int | None = None
    username: str | None = None
    fullname: str | None = None
    profilepicture: str | None = None
    rating: float | None = None
    reviews_count: int | None = None
    rating_count: int | None = None
    is_online: bool | None = None


class Activity(BaseModel):
    views: int | None = None
    orders: int | None = None
    earned: int | None = None


class KworkObject(BaseModel):
    id: int | None = None
    category_id: int | None = None
    category_name: str | None = None
    status_id: int | None = None
    status_name: str | None = None
    title: str | None = None
    url: str | None = None
    image_url: str | None = None
    cover: Cover | None = None
    price: int | None = None
    is_price_from: bool | None = None
    is_from: bool | None = None
    photo: str | None = None
    is_best: bool | None = None
    is_hidden: bool | None = None
    is_favorite: bool | None = None
    lang: str | None = None
    worker: Worker | None = None
    activity: Activity | None = None
    edits_list: list[Any] | None = None
    profile_sort: int | None = None
    is_subscription: bool | None = Field(None, alias="isSubscription")
    badges: list[Any] | None = None
