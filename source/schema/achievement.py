from pydantic import BaseModel


class Achievement(BaseModel):
    id: int | None = None
    name: str | None = None
    description: str | None = None
    image_url: str | None = None
