from base_storage import BaseStorage
from exceptions import ToManyDifferentProductsError


class Shop(BaseStorage):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise ToManyDifferentProductsError

        super().add(name, amount)