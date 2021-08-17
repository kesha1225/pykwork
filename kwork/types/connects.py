from pydantic import BaseModel


class Connects(BaseModel):
    all_connects: int
    active_connects: int
    update_time: int
