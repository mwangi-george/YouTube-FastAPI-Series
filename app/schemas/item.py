from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Item(BaseModel):
    item_id: int
    item_name: str
    item_description: Optional[str]


class ItemEnum(str, Enum):
    electronics = "electronics"
    households = "households"
    furniture = "furniture"


class MultipleItems(BaseModel):
    items: list[Item]


class User(BaseModel):
    username: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
