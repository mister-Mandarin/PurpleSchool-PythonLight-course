# Принять строку формата "<руб> руб <коп> коп" (пример: 100 руб 10 коп)
# и вывести нормализованную сумму в рублях с двумя знаками после запятой: 100.10 ₽.
# Поддержать варианты без копеек ("159 руб" → "159.00 ₽").
# Программа читает одну строку из input()
# Регистр и лишние пробелы игнорируются
# Допустимые слова для единиц
# На выходе — сумма в виде X.YY ₽ (два знака после запятой)
# Если формат некорректный — вывести: Некорректный формат суммы

# RUBLE_SYMBOL = "\u20bd"

# while True:
#     expense = str(
#         input("Введите расход в формате <руб> руб <коп> коп: ")).lower().strip().split()
#     if not 'руб' in expense:
#         print('Некорректный формат суммы!')
#         continue

#     expense = [el for el in expense if el.isdigit()]

#     if not expense:
#         print('Цифры не найдены!')
#         continue

#     if len(expense) == 1:
#         expense.append('0')

#     if len(expense[-1]) > 2:
#         expense[-1] = expense[-1][:2]

#     break

# print(f'{expense[0]}.{int(expense[1]):02d} {RUBLE_SYMBOL}')

MENU = [
    'Меню:',
    '1 - Добавить расход',
    '2 - Показать все расходы',
    '3 - Показать сумму и средний расход',
    '4 - Удалить расход по номеру',
    '5 - Выход'
]

print('\n'.join(MENU))
print(f"{'-'*40}")

while True:
    user_choose = input('Введите пункт меню от 1 до 5: ')
    if user_choose.isdigit() and 1 <= int(user_choose) <= 5:
        print(f"Вы выбрали {MENU[int(user_choose)]}")
        break
    else:
        print('Некорректный ввод!')
