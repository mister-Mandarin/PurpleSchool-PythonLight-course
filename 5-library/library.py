import sys


class LibraryError(Exception):
    pass


BOOKS = [
    {"book": "Война и мир", "author": "Лев Толстой"},
    {"book": "Преступление и наказание", "author": "Фёдор Достоевский"},
    {"book": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"book": "Анна Каренина", "author": "Лев Толстой"},
    {"book": "Герой нашего времени", "author": "Михаил Лермонтов"}
]
# python library.py sort author
# python library.py filter "Толстой"

try:
    action = sys.argv[1]
    param = sys.argv[2]
except IndexError as e:
    print(f'Ошибка: {e}')
    print('Нужно передать 2 параметра: action (sort, filter), param (параметр сортировки или текст фильтра)')
    sys.exit(1)


def print_list_books(data: list[dict]):
    return list(map(lambda x: f"{x['book']} - {x['author']}", data))


try:
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
                    raise LibraryError(
                        'Некорректный параметр сортировки. Доступные параметры: author, book')
        case 'filter':
            if param == '':
                raise LibraryError('Нужно передать текст фильтра')

            filtered = list(filter(lambda x: param in x['author'], BOOKS))

            if len(filtered) == 0:
                raise LibraryError('Ничего не нашлось')
            print(print_list_books(filtered))
        case _:
            raise LibraryError(
                'Некорректная команда. Доступные команды: sort, filter')
except LibraryError as e:
    print(e)


# Нужно обработать все возможные ошибки в помощью ошибок:

# Не передан текст фильтра
# Передана кривая команда
# Передан кривой параметр сортировки
# Сделать базовый класс ошибки и расширить нужными ошибками. Обработать их всех и вывести в консоль ошибки.
