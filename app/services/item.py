from app.schemas.item import Item, ItemEnum


class TestService:
    def __init__(self) -> None:
        pass

    all_items = {
        0: {
            "item_id": 0,
            "item_name": "knife",
            "item_description": "For cutting stuff"
        }
    }

    @staticmethod
    async def get_greeting():
        return {"message": "Hello World"}

    async def get_item(self, item_id: int) -> Item:
        item = self.all_items[item_id]
        return item

    @staticmethod
    async def get_category(item_category: ItemEnum):
        if item_category == ItemEnum.electronics:
            return {"item_category": item_category, "message": "you like electronics"}
        if item_category.value == "furniture":
            return {"item_category": item_category, "message": "you like furniture"}
        if item_category.value == "households":
            return {"item_category": item_category, "message": "you like Households"}
