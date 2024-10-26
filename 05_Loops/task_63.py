"""
Упражнение 63. Среднее значение
(26 строк)
В данном упражнении вы должны написать программу для подсчета
среднего значения всех введенных пользователем чисел. Индикатором
окончания ввода будет служить ноль. При этом программа должна выдавать соответствующее сообщение об ошибке,
если первым же введенным пользователем значением будет ноль.
Подсказка. Поскольку ноль является индикатором окончания ввода, его не нужно
учитывать при расчете среднего.
"""

number = int(input('Enter number or 0 to quit: '))
_sum = 0
count = 0

if number == 0:
    print('Something went wrong...')
else:
    while number != 0:
        _sum += number
        count += 1
        number = int(input('Enter other number:  '))

    average = _sum / count
    print('Average:', average)