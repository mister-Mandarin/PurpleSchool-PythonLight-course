# Ввести три траты: еда, транспорт, развлечения. Вывести общую сумму и среднее - файл expences.py
from decimal import Decimal

sum: Decimal = 0

eat = Decimal(input('Введите траты на еду: '))
sum += eat

drive = Decimal(input('Введите траты на транспорт: '))
sum += drive

funny = Decimal(input('Введите траты на развлечения: '))
sum +=funny

print(f'Общая сумма трат {sum}')
print(f'Средний расход составляет {sum / 3}')
