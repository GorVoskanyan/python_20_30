"""
Такие слова, как первый, второй, третий, являются числительными.
В данном упражнении вам необходимо написать функцию, принимающую на
вход в качестве единственного аргумента целое число и возвращающую
строковое значение, содержащее соответствующее числительное (на английском языке).
Ваша функция должна обрабатывать числа в диапазоне
от 1 до 12. Если входящее значение выходит за границы этого диапазона,
вывод должен оставаться пустым. В основной программе запустите цикл
по натуральным числам от 1 до 12 и выведите на экран соответствующие
им числительные. Ваша программа должна запускаться только в том случае,
если она не импортирована в виде модуля в другой файл.
"""

def int_to_numeral(integer):
    if integer == 1:   return 'first'
    elif integer == 2: return 'second'
    elif integer == 3: return 'third'
    elif integer == 4: return 'fourth'
    elif integer == 5: return 'fifth'
    elif integer == 6: return 'sixth'
    elif integer == 7: return 'seventh'
    elif integer == 8: return 'eighth'
    elif integer == 9: return 'ninth'
    elif integer == 10: return 'tenth'
    elif integer == 11: return 'eleventh'
    elif integer == 12: return 'twelfth'
    else: return 'wrong integer'


if __name__ == '__main__':
    for number in range(1, 14):
        print(number, '->', int_to_numeral(integer=number))

