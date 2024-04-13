from typing import List

class Beer:
    name: str
    price_per_unit: float
    quantity: int
    total: float

    def __init__(self, name: str, price_per_unit: float, quantity: int, total: float):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.total = total


class Item:
    name: str
    price_per_unit: float
    quantity: int
    total: float

    def __init__(self, name: str, price_per_unit: float, quantity: int, total: float):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.total = total


class Round:
    created: str
    items: List[Item]

    def __init__(self, created: str, items: List[Item]):
        self.created = created
        self.items = items


class Order:
    created: str
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[Item]
    rounds: List[Round]

    def __init__(self, created: str, paid: bool, subtotal: float, taxes: float, discounts: float, items: List[Item], rounds: List[Round]):
        self.created = created
        self.paid = paid
        self.subtotal = subtotal
        self.taxes = taxes
        self.discounts = discounts
        self.items = items
        self.rounds = rounds
