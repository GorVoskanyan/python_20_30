# Напишите программу, которая будет запрашивать у пользователя чис
# ла, пока он не пропустит ввод. Сначала на экран должно быть выведено
# среднее значение введенного ряда чисел, после этого друг за другом не
# обходимо вывести список чисел ниже среднего, равных ему (если такие
# найдутся) и выше среднего. Каждый список должен предваряться соот
# ветствующим заголовком

numbers = []
while number:= input(">>>"):
    numbers.append(int(number))
everage = sum(numbers) / len(numbers)
lst_1 = [n for n in numbers if n < everage]
lst_2 = [n for n in numbers if n == everage]
lst_3 = [n for n in numbers if n > everage]
print("%.2f"%everage)
print(*lst_1)
print(*lst_2)
print(*lst_3)