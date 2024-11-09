"""
Напишите программу, которая будет считывать содержимое файла, до
бавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у поль
зователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""

input_file = input('Enter input filename: ')
output_file = input('Enter output filename: ')

with open(input_file, encoding='utf-8') as input_file, open(output_file, 'w', encoding='utf-8') as output_file:
    result = [f"{i}: {line}" for i, line in enumerate(input_file, 1)]
    output_file.writelines(result)


