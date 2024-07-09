from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Query,
)
from typing import Optional
from app.services.item import TestService
from app.schemas.item import Item, ItemEnum


def create_test_router() -> APIRouter:
    router = APIRouter(prefix="/item")
    test_service = TestService()

    @router.get("/")
    async def welcome():
        greeting = await test_service.get_greeting()
        return greeting

    @router.get("/all")
    async def get_multiple_items(start: int = 0, end: int = 5) -> dict:
        items = await test_service.get_several_items(start, end)
        return items

    @router.get("/{item_id}", response_model=Item)
    async def get_item_by_id(item_id: int) -> Item:
        try:
            item = await test_service.get_item(item_id)
            return item
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} does not exist!"
            )

    @router.get("/item_categories/{item_category}")
    async def get_item_category(item_category: ItemEnum):
        response = await test_service.get_category(item_category)
        return response

    @router.post("/", status_code=status.HTTP_201_CREATED)
    async def add_item(item_profile: Item) -> None:
        await test_service.add_item_to_db(item_profile=item_profile)

    @router.put("/{item_id}")
    async def update_item_by_id(item_id: int, item_profile: Item, date: Optional[str] = Query(None, max_length=10, min_length=2, regex="dfv")):
        updated_item_info = await test_service.update_item(item_id=item_id, item_profile=item_profile)
        if date:
            updated_item_info.update({"query": date})
        return updated_item_info

    return router
