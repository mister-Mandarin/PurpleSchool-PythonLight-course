'''
Docstring для taskTracker.commands.py.help
'''


def help_commands():
    print("""
    help - список команд
    add <title> [priority=low|medium|high] [YYY-MM-DD] [tags=tag1,tag2,tag3] - добавить задачу
    remove <id> - удалить задачу
    done <id> - завершить задачу
    edit <id> [title=...] [priority=...] [date=YYYY-MM-DD] [tags=...] - изменить задачу
    tags <id> <tag1,tag2,tag3> - добавить теги к задаче
    list - список задач
    exit - выход
    """)
