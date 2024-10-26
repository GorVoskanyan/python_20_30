"""
В данном упражнении вам нужно написать функцию с именем nextPrime,
которая находит и возвращает первое простое число, большее введенного
числа n. Само число n должно передаваться в функцию в качестве единственного параметра.
В основной программе запросите у пользователя это значение и выведите на экран первое простое число, большее заданного.
Для решения этой задачи импортируйте функцию, созданную в упражнении 98.
"""

from task_98 import is_prime

def next_prime(number):
    number += 1
    while not is_prime(number):
        number += 1

    return number


if __name__ == '__main__':
    number = int(input('>>> '))
    next_prime_number = next_prime(number)
    print('Next prime number is', next_prime_number)