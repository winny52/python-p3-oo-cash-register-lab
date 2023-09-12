class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prices = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.prices.append(price)
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            rounded_discount = round(discount_amount)
            self.total -= rounded_discount
            print(f"After the discount, the total comes to ${self.total}.")
        else:    
            print("There is no discount to apply.")

    def get_all_items(self):
        return self.items

    def void_last_transaction(self):
        if self.items:
            last_item_price = self._get_last_item_price()
            self.total -= last_item_price
            self.items.pop()
        else:
            print("No items to void.")
            self.total = 0.0  # Reset the total to 0 if no items are left

    def _get_last_item_price(self):
        last_item = self.items[-1]
        # Use the item_prices dictionary to look up the price of the last_item.
        return self.get_price_for_item(last_item)

    def get_price_for_item(self, item_title):
        # For demonstration purposes, we'll use a dictionary to store item prices.
        item_prices = {
            "eggs": 0.98,
            "book": 5.00,
            "Lucky Charms": 4.5,
            "Ritz Crackers": 5.0,
            # ... add more items and prices as needed ...
        }

        # Use the dictionary's get() method to retrieve the price for the given item_title.
        # Provide a default value of 0.0 if the item_title is not found in the dictionary.
        return item_prices.get(item_title, 0.0)