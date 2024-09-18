from abc import ABC, abstractmethod
from Product import Product


class InventoryInterface(ABC):

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def remove_product(self, product_name: str) -> None:
        pass

    @abstractmethod
    def get_product_by_name(self, product_name: str) -> Product:
        pass

    @abstractmethod
    def get_total_inventory_value(self) -> float:
        pass

    def is_product_exists(self, product) -> bool:
        pass
