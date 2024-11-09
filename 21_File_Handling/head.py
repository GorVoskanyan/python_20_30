""""
В операционных системах на базе Unix обычно присутствует утилита с на
званием head. Она выводит первые десять строк содержимого файла, имя
которого передается в качестве аргумента командной строки. Напиши
те программу на Python, имитирующую поведение этой утилиты. Если
файла, указанного пользователем, не существует, или не задан аргумент
командной строки, необходимо вывести соответствующее сообщение об
ошибке."""

import sys

try:
    filename = sys.argv[1]
    with open(filename, encoding='utf-8') as file:
        print(''.join(file.readlines()[:10]))
except IndexError:
    print('Filename must be provided as command line parameter.')
except FileNotFoundError as msg:
    print('Unknown file', msg)