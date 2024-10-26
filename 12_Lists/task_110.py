"""
Напишите программу, которая будет запрашивать у пользователя целочисленные значения и сохранять их в виде списка.
Индикатором окончания ввода значений должен служить ноль.
Затем программа должна вывести на экран все введенные пользователем числа (кроме нуля) в порядке
возрастания – по одному значению в строке. Используйте для сортировки либо метод sort, либо функцию sorted.
"""

numbers = []

number = int(input('Enter first number: '))

while number != 0:
    numbers.append(number)
    number = int(input('Enter number: '))

print(numbers)
numbers.sort(reverse=True)
print(numbers)

for number in numbers:
    print(number)