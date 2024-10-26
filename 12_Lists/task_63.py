"""
В данном упражнении вы должны написать программу для подсчета
среднего значения всех введенных пользователем чисел. Индикатором
окончания ввода будет служить ноль. При этом программа должна выдавать соответствующее сообщение об ошибке,
если первым же введенным пользователем значением будет ноль.
"""

number = int(input('Enter number: '))
if number == 0:
    print('First number must be a non zero.')
else:
    gumar = 0
    tveri_qanak = 0
    while number != 0:
        gumar += number
        tveri_qanak += 1
        number = int(input('Enter number: '))

    print(gumar / tveri_qanak)
