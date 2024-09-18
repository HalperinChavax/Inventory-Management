Inventory Management System
Overview
This Python program implements a simple inventory management system. 
The system is designed to manage a collection of products, allowing you to add, remove, and retrieve products, as well as calculate the total inventory value.

Components
Inventory Class
The Inventory class inherits from InventoryInterface and ABC (Abstract Base Class). It provides the following functionality:

add_product(product: Product) -> None: Adds a new product to the inventory if it does not already exist.
remove_product(product_name: str) -> None: Removes a product from the inventory by its name.
get_product_by_name(product_name: str) -> Product: Retrieves a product from the inventory by its name. Raises a ValueError if the product is not found.
get_total_inventory_value() -> float: Calculates and returns the total value of all products in the inventory.
is_product_exist(product_name) -> bool: Checks if a product exists in the inventory and prints a message if it does.

Usage
1. Create an Inventory Instance:
    inventory = Inventory()
2. Add Products:
   product = Product(name="Example Product", price=100.0)
    inventory.add_product(product)
3. Remove Products:
    inventory.remove_product("Example Product")
4. Retrieve Products:
    product = inventory.get_product_by_name("Example Product")
5. Calculate Total Inventory Value:
    total_value = inventory.get_total_inventory_value()
   
Dependencies
  InventoryInterface (assumed to be defined in a separate file)
  Product (assumed to be defined in a separate file)
