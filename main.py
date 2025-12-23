# Проект - менеджер задач

def main():
    print('Привет! Это менеджер задач!')
    print('help - список команд')

    while True:
        try:
            user_input = input('> ').strip()
            parts = user_input.split()
            cmd, *args = parts

            match cmd:
                case 'help':
                    print('help - список команд')
                case 'add':
                    pass
                case 'remove':
                    pass
                case 'edit':
                    pass
                case 'tags':
                    pass
                case 'exit':
                    print('Программа завершена')
                    break
                case _:
                    print('Неизвестная команда')
        except KeyboardInterrupt:
            print('\nПрограмма завершена...')
            break
        except Exception as e:
            print("Ошибка:", e)


main()
