from pydantic import BaseModel, Field
from typing import Optional


class Item(BaseModel):
    item_id: int
    item_name: str
    item_description: Optional[str]
