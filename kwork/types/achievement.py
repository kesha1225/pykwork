from pydantic import BaseModel


class Achievement(BaseModel):
    id: int
    name: str
    description: str
    image_url: str
