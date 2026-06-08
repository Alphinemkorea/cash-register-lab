class CashRegister:
    def __init__(self, discount=0):
        # validate discount
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            discount = 0

        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "item": title,
            "price": price,
            "quantity": quantity
        })

        return self.items

    def apply_discount(self):
        # if no discount OR no items
        if self.discount == 0:
            print("There is no discount to apply.")
            return self.total

        # apply discount correctly
        self.total = self.total - (self.total * self.discount / 100)

        # IMPORTANT: must match exact formatting (no .00)
        print(f"After the discount, the total comes to ${int(self.total)}.")

        return self.total

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            self.total = 0.0
            return self.total

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])

        return self.total