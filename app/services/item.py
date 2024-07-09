from app.schemas.item import Item


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
