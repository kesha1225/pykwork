from typing import List, Dict, Union

from pydantic import BaseModel, Field


class PortfolioItem(BaseModel):
    id: int = None
    title: str = None
    order_id: Union[int, str] = None
    category_id: int = None
    category_name: str = None
    item_type: str = Field(None, alias="type")
    photo: str = None
    video: str = None
    likes: int = None
    likes_dirty: int = None
    views: int = None
    views_dirty: int = None
    comments_count: int = None
    is_liked: bool = None
    images: List[Dict] = None
    videos: List[Dict] = None
    duplicate_from: str = None
