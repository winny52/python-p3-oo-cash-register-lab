#!/usr/bin/env python3

class CashRegister:
  pass
  def __init__(self):
        self.total = 0
        self.last_transaction_amount = 0

  def add_item(self, price):
        self.total += price
        self.last_transaction_amount = price

  def apply_discount(self, discount_percentage):
        if discount_percentage > 0 and discount_percentage <= 100:
            discount = self.total * (discount_percentage / 100)
            self.total -= discount
            return self.total
        else:
            print("Invalid discount percentage")
            return None

  def void_last_transaction(self):
        if self.last_transaction_amount > 0:
            self.total -= self.last_transaction_amount
            self.last_transaction_amount = 0
        else:
            print("No transaction to void")