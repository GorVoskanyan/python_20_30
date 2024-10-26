"""
В данном упражнении вам необходимо написать функцию, проверяющую введенный пароль на надежность.
Определим как надежный пароль, состоящий минимум из восьми символов и включающий хотя бы по одной
букве в верхнем и нижнем регистрах и как минимум одну цифру.
Функция должна возвращать True, если переданный в качестве параметра пароль отвечает требованиям надежности.
В противном случае возвращаемым значением должно быть False.
В основной программе необходимо запросить у пользователя пароль и оповестить его о том,
является ли он достаточно надежным. Программа должна запускаться только в том случае,
если она не импортирована в виде модуля в другой файл.
"""
import task_100

def is_valid_password(password):
    if len(password) < 8:
        return False

    upper = lower = digit = 0

    for symbol in password:
        if symbol.isdigit():
            digit += 1
        elif symbol.isupper():
            upper += 1
        elif symbol.islower():
            lower += 1

        if upper and lower and digit:
            return True
    return False


if __name__ == '__main__':
    password = task_100.password_generator()
    if is_valid_password(password):
        print(password, 'is valid.')
    else:
        print(password, 'is not valid.')