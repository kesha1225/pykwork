from pydantic import BaseModel


class Category(BaseModel):
    """Базовая категория кворков (третий уровень)."""

    id: int | None = None
    name: str | None = None
    description: str | None = None


class SubCategory(Category):
    """Подкатегория второго уровня с вложенными категориями."""

    subcategories: list[Category] | None = None


class ParentCategory(Category):
    """Родительская категория первого уровня."""

    subcategories: list[SubCategory] | None = None
