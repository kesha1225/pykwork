import typing

from pydantic import BaseModel, validator


class Subcategory(BaseModel):
    id: int = None
    name: str = None
    description: typing.Optional[str] = None


def normalize_subcategories(subcategories: typing.List[dict]):
    return [Subcategory(**dict_category) for dict_category in subcategories]


class Category(BaseModel):
    id: int = None
    name: str = None
    description: typing.Optional[str] = None
    subcategories: typing.List[typing.Union[dict, Subcategory]] = None

    _normalize_subcategories = validator("subcategories", allow_reuse=True)(
        normalize_subcategories
    )
