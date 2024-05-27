#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, item_name, price, quantity=1):
        self.items.append((item_name, price, quantity))
        self.total += price * quantity

    def apply_discount(self):
        if self.discount:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_item(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1] * last_item[2]