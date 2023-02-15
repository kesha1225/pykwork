from typing import Optional

from pydantic import BaseModel


class KworkMinObject(BaseModel):
    # TODO в файлик вынести
    id: int = None
    title: str = None
    active: int = None
    feat: bool = None


class Writer(BaseModel):
    id: int = None
    username: str = None
    profilepicture: str = None


class Review(BaseModel):
    id: int = None
    time_added: int = None
    text: str = None
    auto_mode: Optional[str] = None
    good: bool = None
    bad: bool = None
    kwork: KworkMinObject = None
    writer: Writer = None
