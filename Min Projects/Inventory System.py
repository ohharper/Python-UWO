class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0
            print(f"Quantity for '{self.name}' cannot be negative. Set to 0.")
        print(f"Updated quantity for '{self.name}': {self.quantity}")

    def total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added '{product.name}' to the inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total_value = sum(product.total_value() for product in self.products)
        return total_value


if __name__ == "__main__":
    inventory = Inventory()

    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.99, 20)
    product3 = Product("Headphones", 89.99, 50)

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    inventory.display_inventory()

    product1.update_quantity(-11)
    product2.update_quantity(5)

    inventory.display_inventory()

    total_value = inventory.total_inventory_value()
    print(f"\nTotal value of inventory: ${total_value}")
