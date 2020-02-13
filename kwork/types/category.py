from pydantic import BaseModel, validator
import typing


class Subcategory(BaseModel):
    id: int
    name: str
    description: typing.Optional[str]


def normalize_subcategories(subcategories: typing.List[dict]):
    return [Subcategory(**dict_category) for dict_category in subcategories]


class Category(BaseModel):
    id: int
    name: str
    description: str
    subcategories: typing.List[dict]

    _normalize_subcategories = validator("subcategories", allow_reuse=True)(
        normalize_subcategories
    )
