# Калькулятор скидки. Спросить у пользователя цену товара. Спросить процент скидки. Посчитать и вывести цену со скидкой. - файл discount.py
from decimal import Decimal

price = Decimal(input("Введите цену товара: "))

discount_percent = Decimal(input("Введите процент скидки: "))

discount_amount = price * discount_percent / 100
discounted_price = price - discount_amount

print(f"Цена со скидкой: {discounted_price}")