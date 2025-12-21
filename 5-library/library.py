import sys

BOOKS = [
    {"title": "Война и мир", "author": "Лев Толстой"},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский"},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"title": "Анна Каренина", "author": "Лев Толстой"},
    {"title": "Герой нашего времени", "author": "Михаил Лермонтов"}
]
# python library.py sort author
# python library.py filter "Толстой"

action = sys.argv[1]
param = sys.argv[2]

match action:
    case 'sort':
        match param:
            case 'author':
                print(sorted(BOOKS, key=lambda x: x['author']))
            case 'title':
                print(sorted(BOOKS, key=lambda x: x['title']))
            case _:
                print('Некорректный ввод!')
    case 'filter':
        print(list(filter(lambda x: param in x['author'], BOOKS)))
    case _:
        print('Некорректный ввод!')
