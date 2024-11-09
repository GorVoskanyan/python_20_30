try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    res = a / b
    print(res)
except ValueError as msg:
    print('Please enter a integer.', msg)
except ZeroDivisionError as exc:
    print('b must be non zero.', exc)

while True:
    try:
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        print(a + b)
        break
    except ValueError as msg:
        print(msg)

# raise ValueError('My value error')

class MyError(Exception):
    pass

raise MyError('My first exception')
