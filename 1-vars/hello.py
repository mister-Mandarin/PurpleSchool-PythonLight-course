# Спросить у пользователя имя и возраст последовательно.
# Сохранить результаты в переменные.
# Вывести строку: «Привет, <имя>! Тебе <возраст> лет». Называем скрипт - hello.py
condition: bool = False
name: str = ''
age: int = 0 

while not condition: 
    name = input("Введите ваше ИМЯ. Максимум 15 символов: ")
    if name.isalpha() and len(name) <=15:
        condition = True
    else: 
        print('Имя содержит недопустимые символы или слишком длинное. Повторите ввод.')
        break

    age = input('Введите ваш ВОЗРАСТ. Сколько вам полных лет:')
    if age.isdigit() and 0 < int(age) < 100:
        condition = True
    else:
        print('Недопустимый возраст')
        break


print(f'Привет, {name}! Тебе {age} лет.')