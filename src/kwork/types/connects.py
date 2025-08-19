from pydantic import BaseModel


class Connects(BaseModel):
    all_connects: int = None
    active_connects: int = None
    update_time: int = None
