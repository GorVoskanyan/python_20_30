"""
Напишите рекурсивную функцию, переводящую неотрицательное
целое число в двоичную систему. Воспринимайте 0 и 1 как базовые слу
чаи с возвратом соответствующего строкового значения. Для остальных
положительных чисел n вам необходимо вычислить следующую цифру
при помощи оператора взятия остатка от деления и затем осуществить
рекурсивный вызов с вычислением цифр для n // 2. Наконец, вам нужно
сцепить строковый результат рекурсивного вызова со следующей цифрой,
которую заранее надо преобразовать в строку, и вернуть полученную
строку в качестве результата функции.
Напишите основную программу, которая будет использовать рекурсивную
функцию для преобразования неотрицательного числа, введенного
пользователем, из десятичной системы счисления в двоичную. Если будет
введено отрицательное значение, программа должна вывести соответствующее сообщение об ошибке.
"""

def int_to_binary(n):
    return str(n) if n <= 1 else int_to_binary(n // 2) + str(n % 2)

bin_13 = int_to_binary(13)
print(bin(13))
print(bin_13)