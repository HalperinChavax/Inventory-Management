import pytest
from Inventory import Inventory
from Product import Product


@pytest.fixture
def inventory():
    return Inventory()


@pytest.fixture
def product():
    return Product("Cherry", 10.0)


def test_add_product(inventory, product):
    inventory.add_product(product)
    assert len(inventory.products) == 1


def test_get_product_by_name(inventory, product):
    inventory.add_product(product)
    assert inventory.get_product_by_name("Cherry") == product


def test_remove_product(inventory, product):
    inventory.add_product(product)
    len_before_remove = len(inventory.products)
    inventory.remove_product("Cherry")
    assert len(inventory.products) == len_before_remove - 1


def test_get_total_inventory_value(inventory):
    prod1 = Product("Cherry", 10.0)
    prod2 = Product("Apple", 5.0)
    prod3 = Product("Banana", 2.1)

    inventory.add_product(prod1)
    inventory.add_product(prod2)
    inventory.add_product(prod3)

    assert inventory.get_total_inventory_value() == 17.1
