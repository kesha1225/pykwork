from pydantic import BaseModel


class KworkMinObject(BaseModel):
    id: int | None = None
    title: str | None = None
    active: int | None = None
    feat: bool | None = None


class Writer(BaseModel):
    id: int | None = None
    username: str | None = None
    profilepicture: str | None = None


class Review(BaseModel):
    id: int | None = None
    time_added: int | None = None
    text: str | None = None
    auto_mode: str | None = None
    good: bool | None = None
    bad: bool | None = None
    kwork: KworkMinObject | None = None
    writer: Writer | None = None
