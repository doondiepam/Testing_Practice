class ShoppingCart:

    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

        return self.items

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError("Item not found")
        del self.items[name]
        return self.items

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def clear_cart(self):
        self.items = {}
        return self.items
