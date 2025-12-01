from pydantic import BaseModel


class Connects(BaseModel):
    all_connects: int | None = None
    active_connects: int | None = None
    update_time: int | None = None
