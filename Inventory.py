from abc import ABC

from InventoryInterface import InventoryInterface
from Product import Product


class Inventory(InventoryInterface, ABC):
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product) -> None:
        if not self.is_product_exist(product.name):
            self.products[product.name] = product

    def remove_product_by_name(self, product_name: str) -> None:
        if self.get_product_by_name(product_name):
            del self.products[product_name]

    def get_product_by_name(self, product_name: str) -> Product:
        if self.is_product_exist(product_name):
            return self.products[product_name]
        raise ValueError(f"Product '{product_name}' not found in the inventory.")

    def get_total_inventory_value(self) -> float:
        return sum(product.price for product in self.products.values())

    def is_product_exist(self, product_name) -> bool:
        if product_name in self.products:
            print(f"Product '{product_name}' already exists in the inventory.")
            return True
        return False
