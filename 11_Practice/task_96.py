"""
В данном упражнении вам предстоит написать функцию с именем isInteger, определяющую,
представляет ли введенная строка целочисленное значение. При проверке вы можете игнорировать ведущие и
замыкающие пробелы в строке. После исключения лишних пробелов строку можно считать представляющей целое число,
если ее длина больше или равна одному символу и она целиком состоит из цифр. Возможен также вариант
с ведущим знаком «+» или «-», после которого должны идти цифры.
В основной программе у пользователя должна запрашиваться исходная
строка и выводиться сообщение о том, можно ли введенное значение воспринимать как целое число.
Убедитесь, что основная программа не будет запускаться, если файл импортирован в другой файл в качестве модуля.
"""

def is_integer(text):
    if text[0] == '+' or text[0] == '-':
        text = text[1:]

    for char in text:
        if not char.isdigit():
            return False
    return True


text = input('>>> ')
if is_integer(text):
    print(text, 'is number.')
else:
    print(text, 'is not number.')