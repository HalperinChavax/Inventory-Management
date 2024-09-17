import pytest
from Inventory import Inventory
from Product import Product

@pytest.fixture
def cart():
    return Inventory()

def test_add_product(cart):
    prod = Product("Cherry", 10)
    cart.add_product(prod)
    assert len(cart.products) == 1

def test_when_product_added_then_cart_contains_product(cart):
    prod = Product("Cherry", 10)
    cart.add_product(prod)
    assert cart.get_product(prod.name) == prod

def test_remove_product(cart):
    prod = Product("Cherry", 10)
    cart.add_product(prod)
    len_before_remove = len(cart.products)
    print(len_before_remove)
    cart.remove_product("Cherry")
    assert len(cart.products) < len_before_remove

def test_get_product(cart):
    prod = Product("Cherry", 10)
    cart.add_product(prod)
    assert cart.get_product("Cherry") == prod

def test_get_total_inventory_value(cart):
    prod1 = Product("Apple", 5.0)
    prod2 = Product("Banana", 2.1)
    prod3 = Product("Cherry", 10.0)
    cart.add_product(prod1)
    cart.add_product(prod2)
    cart.add_product(prod3)
    assert cart.get_total_inventory_value() == 17.1