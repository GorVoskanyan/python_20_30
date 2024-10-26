# x = int(input('>>> '))
#
# if x > 0:
#     print('Positive')
# elif x == 0:
#     print('Zero')
# else:
#     print('Negative')


# logical operators
# and, or, not

# x = 9
# if 10 > 4 and 0 < 10 and 1 > 10 and x < 90:
#     print('1')
# elif 1 < -1 or 1 > 10 or -1 > 0 or -0.9 > 2:
#     print('0')
# else:
#     print(not(False))


# if True or False and True and False:
#     print('1')


# nested conditions
# x = int(input('>>> '))
#
# if x % 2 == 0:
#     print(x, 'is even')
#     if x > 0:
#         print(x, 'is positive')
#     else:
#         print(x, 'is negative')
# else:
#     print(x, 'is odd')


# ternary operator
# x = int(input('>>> '))

# if x == '1':
#     is_rain = 'Yes'
# elif x == '0':
#     is_rain = 'No'
# else:
#     is_rain = 'Invalid input'

# is_rain = 'Yes' if x == '1' else 'No' if x == '0' else 'Invalid input'
# print(is_rain)

# print(id(x))
# print(id(1))
# y = 1
# print(x is y)

x, y = 1, 0
if x > 10:
    if y > -1:
        print('ok')
elif 1 > 0:
    print('1')
