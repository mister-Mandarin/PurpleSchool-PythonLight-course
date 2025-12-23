'''
Работа с заказами
'''

from typing import TypedDict

STATUSES = ['new', 'in_progress', 'done', 'canceled']


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: list[str]
    due: str | None
    created_at: str
    closed_at: str


def create_order():
    pass


def list_orders():
    pass


def edit_order():
    pass


def remove_order():
    pass
