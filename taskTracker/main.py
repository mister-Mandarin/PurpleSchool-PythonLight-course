# Проект - менеджер задач
from commands.help import help_commands
from commands.tasks import make_task


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
                    help_commands()
                case 'add':
                    pass
                case 'remove':
                    pass
                case 'done':
                    pass
                case 'edit':
                    pass
                case 'tags':
                    pass
                case 'list':
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


if __name__ == '__main__':
    main()
