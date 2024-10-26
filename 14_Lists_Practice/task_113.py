"""
В данном упражнении вам предстоит разработать программу, в которой
у пользователя будет запрошен список слов, пока он не оставит строку
ввода пустой. После этого на экране должны быть показаны слова, введенные пользователем, но без повторов, – каждое по одному разу. При этом
слова должны быть отображены в том же порядке, в каком их вводили
с клавиатуры. Например, если пользователь на запрос программы введет
следующий список слов:
first
second
first
third
second
программа должна вывести:
first
second
third
"""

data = []

while word := input('Enter word or return: '):
    if word not in data:
        data.append(word)

# for word in data:
#     print(word)

# print(data)