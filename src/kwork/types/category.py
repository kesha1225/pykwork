from __future__ import annotations

from pydantic import BaseModel, validator


class Subcategory(BaseModel):
    id: int = None
    name: str = None
    description: str | None = None


def normalize_subcategories(subcategories: list[dict]):
    return [Subcategory(**dict_category) for dict_category in subcategories]


class Category(BaseModel):
    id: int = None
    name: str = None
    description: str | None = None
    subcategories: list[dict | Subcategory] = None

    _normalize_subcategories = validator("subcategories", allow_reuse=True)(
        normalize_subcategories,
    )
