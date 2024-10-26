# for loops

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# for <variable> in <iterable>:
#   ...

# for i in -3, 65, 71, -903:
#     print(i)

# text = 'python is powerful!'
# changed_text = ''
#
# for char in text:
#     # print(char + '|', end='\n')
#     if char == ' ':
#         continue
#     elif char == '!':
#         break
#     changed_text += char
#
# print(changed_text)

# for num in '123':
#     print(num, type(num))

# num = '123'
# print(num[0])
# print(num[1])
# print(num[2])


# range(start, stop, step) function
# one_to_ten = range(1, 10)
# print(one_to_ten)

# for num in range(65, 98):
    # print(num)
    # print(chr(num))


# for num in range(10):
#     print(num)
# start = int(input('>>> '))
# stop = int(input('>>> '))

# for even_num in range(start, stop + 1, 2):
    # even_num = float(even_num)
    # print(even_num)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end='\t')
#     print()


# pin = input('Enter pin! ')
#
# while pin != '1793':
#     print('Wrong pin')
#     pin = input('Enter pin! ')
#


# while True:
#     for _ in range(3):
#         pin = input('Enter pin! ')
#         if pin == '1111':
#             print('Welcome!')
#             break
#     else:
#         print('Blocked!')
#
#     print('Next client')


# indexing
# text = 'internationalization'
# first = text[0]
# last = text[-1]
# print(first)
# print(last)


# for i in range(10, 0, -1):
#     print(i)