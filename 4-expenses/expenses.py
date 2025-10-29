def add_expense() -> str:
    while True:
        expense = str(
            input("Введите расход в формате <руб> руб <коп> коп: ")).lower().strip().split()
        if not 'руб' in expense:
            print('Некорректный формат суммы!')
            continue

        expense = [el for el in expense if el.isdigit()]

        if not expense:
            print('Цифры не найдены!')
            continue

        if len(expense) == 1:
            expense.append('0')

        if len(expense[-1]) > 2:
            expense[-1] = expense[-1][:2]

        break

    return f'{expense[0]}.{int(expense[1]):02d} {"\u20bd"}'


def show_menu() -> int:
    print(f"{'-'*40}")
    menu = [
        'Меню:',
        '1 - Добавить расход',
        '2 - Удалить расход',
        '3 - Общая сумма расходов',
        '4 - Средний расход',
        '5 - Красивый отчёт по расходам',
        '6 - Выход'
    ]

    print('\n'.join(menu))
    print(f"{'-'*40}")

    while True:
        user_choose = input('\nВведите пункт меню от 1 до 6: ')

        if user_choose.isdigit() and 1 <= int(user_choose) <= 6:
            print(f"\nВы выбрали {menu[int(user_choose)]}")
            break

        print('Некорректный ввод!')

    return int(user_choose)


def exit_program() -> None:
    print(
        "\nПроисходит выход из программы.\n"
        "Все введённые данные будут удалены.\n"
        "Досвидания!"
    )


def delete_expence(expenses: list[str]) -> int:
    if len(expenses) == 0:
        print('Список расходов пуст!')
        return 0

    print_report(expenses)

    while True:
        chose = input('Введите индекс для удаления расхода: ')

        if chose.isdigit() and int(chose) < len(expenses):
            return int(chose)


def print_report(expenses: list[str]) -> None:
    print('\nСписок ваших расходов')

    for i, el in enumerate(expenses):
        print(f'Индекс: {i} - значение {el}')


def get_sum(expenses: list[str]) -> float:
    total = sum(float(el[:-2]) for el in expenses)
    return round(total, 2)


def get_total(expenses: list[str]) -> None:
    if len(expenses) == 0:
        print('Список расходов пуст!')
        return

    total_sum: float = get_sum(expenses)

    print(f'Общая сумма расходов {total_sum} {"\u20bd"}')


def get_average(expenses: list[str]) -> None:
    if len(expenses) == 0:
        print('Список расходов пуст!')
        return

    total_sum: float = get_sum(expenses)

    print(f'Средний расход {total_sum / len(expenses)} {"\u20bd"}')


def main():
    expenses: list[str] = []

    while True:
        chose = show_menu()
        match chose:
            case 1:  # Добавить расход
                expenses.append(add_expense())
            case 2:  # Удалить расход
                del_index = delete_expence(expenses)
                if del_index == 0:
                    continue
                expenses.pop()
            case 3:  # Сумма расходов
                get_total(expenses)
            case 4:  # Средний расход
                get_average(expenses)
            case 5:  # Отчет
                print_report(expenses)
            case 6:  # Выход
                exit_program()
                break
            case _: pass


main()
# add_expense(expenses, value) — добавляет расход
# delete_expence(expenses, index) — удалить расход
# get_total(expenses) — возвращает сумму
# get_average(expenses) — возвращает средний расход
# print_report(expenses) — печатает красивый отчёт
