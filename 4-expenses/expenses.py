# Создать список из трат за неделю (7 чисел)
# Посчитать сумму, среднее, минимум и максимум.
# Сохранить в кортеже (минимум, максимум, сумма) и вывести его.

expenses = [22.22, 33.5, 104.34, 299.99, 4321.21, 12.36, 98.89 ]
result = []

result.append(min(expenses))
result.append(max(expenses))
result.append(sum(expenses))

print(tuple(result))