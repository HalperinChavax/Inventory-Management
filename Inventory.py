from Product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return f"Product '{product_name}' removed successfully."
        return f"Product '{product_name}' not found in the inventory."

    def get_product(self,product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return f"Product '{product_name}' not found in the inventory."

    def get_total_inventory_value(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price

