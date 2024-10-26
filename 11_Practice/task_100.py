"""
Напишите функцию, которая будет генерировать случайный пароль.
В пароле должно быть от 7 до 10 символов, при этом каждый символ должен
быть случайным образом выбран из диапазона от 33 до 126 в таблице ASCII.
Ваша функция не должна принимать на вход параметры, а возвращать будет сгенерированный пароль.
В основной программе вы должны просто вывести созданный случайным образом пароль.
Программа должна запускаться только в том случае, если она не импортирована в виде модуля в другой файл.
"""
import random


def password_generator():
    password_length = random.randint(7, 10)
    password = ''

    for _ in  range(password_length):
        random_number = random.randint(33, 126)
        random_char = chr(random_number)
        password += random_char

    return password

if __name__ == '__main__':
    password = password_generator()
    print(password)