'''
Спросить у пользователя категорию: «напиток», «суп», «десерт».
В зависимости от выбора — предложить варианты (например:
    •    напиток → «чай», «кофе», «сок»
    •    суп → «борщ», «щи», «суп-пюре»
    •    десерт → «торт», «мороженое», «фрукты»).
Пользователь вводит конкретное блюдо.
Программа с помощью match case выводит цену выбранного блюда.
'''
category = ['Выберите категорию:', '1 - напиток', '2 - суп', '3 - десерт']

items = {
    category[1]: {'чай': 50, 'кофе': 70, 'сок': 60},
    category[2]: {'борщ': 80, 'щи': 75, 'суп-пюре': 90},
    category[3]: {'торт': 120, 'мороженое': 100, 'фрукты': 85}
}

for key in category:
    print(key)

chose_category = int(input('Выберите категорию, введите число от 1 до 3: '))

chose_category = category[chose_category]
category_items = items[chose_category]

print(f'Вы выбрали категорию {chose_category}')
print('Вам доступны следующие товары:')

for key, value in category_items.items():
    print(f'Товар: {key} Стоимость: {value}')

chose_item = str(input('Напишите название выбранного товара: '))

for k, v in category_items.items():
    match k:
        case k if k == chose_item:
            print(f'Товар {chose_item} вам будет стоить {v}')
        case _:
            continue
