import sys

BOOKS = [
    {"book": "Война и мир", "author": "Лев Толстой"},
    {"book": "Преступление и наказание", "author": "Фёдор Достоевский"},
    {"book": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"book": "Анна Каренина", "author": "Лев Толстой"},
    {"book": "Герой нашего времени", "author": "Михаил Лермонтов"}
]
# python library.py sort author
# python library.py filter "Толстой"

action = sys.argv[1]
param = sys.argv[2]


def print_list_books(data: list[dict]):
    return list(map(lambda x: f"{x['book']} - {x['author']}", data))


match action:
    case 'sort':
        match param:
            case 'author':
                sorted_by_author = sorted(BOOKS, key=lambda x: x['author'])
                print(print_list_books(sorted_by_author))
            case 'book':
                sorted_by_book = sorted(BOOKS, key=lambda x: x['book'])
                print(print_list_books(sorted_by_book))
            case _:
                print('Некорректный ввод!')
    case 'filter':
        filtered = list(filter(lambda x: param in x['author'], BOOKS))
        print(print_list_books(filtered))
    case _:
        print('Некорректный ввод!')
