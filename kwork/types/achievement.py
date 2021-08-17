from pydantic import BaseModel


class Achievement(BaseModel):
    id: int = None
    name: str = None
    description: str = None
    image_url: str = None
