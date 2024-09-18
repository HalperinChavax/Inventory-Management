import pytest
from Inventory import Inventory
from Product import Product

@pytest.fixture
def cart():
    return Inventory()

@pytest.fixture
def product():
    return Product("Cherry", 10.0)

def test_add_product(cart, product):
    cart.add_product(product)
    assert len(cart.products) == 1

def test_get_product(cart, product):
    cart.add_product(product)
    assert cart.get_product("Cherry") == product

def test_remove_product(cart, product):
    cart.add_product(product)
    len_before_remove = len(cart.products)
    cart.remove_product("Cherry")
    assert len(cart.products) == len_before_remove - 1

def test_get_total_inventory_value(cart):
    prod1 = Product("Apple", 5.0)
    prod2 = Product("Banana", 2.1)
    prod3 = Product("Cherry", 10.0)

    cart.add_product(prod1)
    cart.add_product(prod2)
    cart.add_product(prod3)

    assert cart.get_total_inventory_value() == 17.1