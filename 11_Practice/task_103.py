"""
Используя решения из упражнений 100 и 102, напишите программу, генерирующую случайный надежный пароль и
выводящую его на экран. Посчитайте, с какого раза удастся создать пароль, отвечающий нашим
требованиям надежности, и выведите на экран количество попыток.
Импортируйте функции из предыдущих упражнений и вызывайте их при необходимости для решения этой задачи.
"""

from task_102 import is_valid_password
from task_100 import password_generator


password = password_generator()
count = 1
while not is_valid_password(password):
    count += 1
    password = password_generator()


valid_password = password
print(count)
print(valid_password)