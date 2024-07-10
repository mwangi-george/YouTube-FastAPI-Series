from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Query,
    Path,
    Body,
)
from typing import Optional
from app.services.item import TestService
from app.schemas.item import (
    Item,
    ItemEnum,
    User,
)


def create_test_router() -> APIRouter:
    router = APIRouter(prefix="/item")
    test_service = TestService()

    @router.get("/")
    async def welcome():
        greeting = await test_service.get_greeting()
        return greeting

    @router.get("/items")
    async def get_items(q: list[str] = Query(["foo", "fuu"], deprecated=True)):
        result = {
            "items": [{"item_id": "foo"}, {"item_id": "far"}, {"item_id": "bar"}]
        }
        if q:
            result.update({"item_id": q})
        return result

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
    async def update_item_by_id(
        item_id: int,
        item_profile: Item,
        q: Optional[str] = Query(
            None,
            max_length=10,
            min_length=2,
            regex="dfv",
            alias="item-query"
        )
    ):
        updated_item_info = await test_service.update_item(item_id=item_id, item_profile=item_profile)
        if q:
            updated_item_info.update({"query": q})
        return updated_item_info

    @router.get("/items_validation/{item_id}")
    async def read_items_validation(
        # this makes the rest of the arguments to be keyword arguments (kwargs)
        *,
        # ... makes it a required parameter not set to any value
        item_id: int = Path(..., title="The id of the item", ge=50, le=500),
        q: str,
        size: float = Query(..., ge=0, le=1)
    ):
        results = {"item_id": item_id, "size": size}
        if q:
            results.update({"q": q})
        return results

    @router.put("/multiple_query_params/{item_id}")
    async def update_multiple_params(
        *,
        item_id: int = Path(..., ge=1, le=100),
        q: str | None = None,
        item: Item | None,
        user: User | None = None,
        # passing a single value in the request body
        importance: int = Body(...)
    ):
        results = {"item_id": item_id}
        if q:
            results.update({"q": q})
        if item:
            results.update({"item": item})
        if user:
            results.update({"user": user})
        if importance:
            results.update({"importance": importance})
        return results

    return router
