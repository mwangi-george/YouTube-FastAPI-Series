from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from app.services.item import TestService
from app.schemas.item import Item, ItemEnum


def create_test_router() -> APIRouter:
    router = APIRouter(prefix="/item")
    test_service = TestService()

    @router.get("/")
    async def welcome():
        greeting = await test_service.get_greeting()
        return greeting

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

    return router
