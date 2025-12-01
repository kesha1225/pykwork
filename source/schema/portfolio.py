from typing import Any

from pydantic import BaseModel, Field


class PortfolioItem(BaseModel):
    id: int | None = None
    title: str | None = None
    order_id: int | str | None = None
    category_id: int | None = None
    category_name: str | None = None
    item_type: str | None = Field(None, alias="type")
    photo: str | None = None
    video: str | None = None
    likes: int | None = None
    likes_dirty: int | None = None
    views: int | None = None
    views_dirty: int | None = None
    comments_count: int | None = None
    is_liked: bool | None = None
    images: list[dict[str, Any]] | None = None
    videos: list[dict[str, Any]] | None = None
    duplicate_from: str | None = None
