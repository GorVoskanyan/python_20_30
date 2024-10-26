from task_85 import pifagor

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def main():
    while True:
        a = input('Enter first number or quit: ')
        if a == 'quit':
            print('Bye-Bye')
            break
        a = float(a)
        b = float(input('Enter second number: '))
        operator = input('\n1. +\n2. -\n3. *\n4. :\n5. Pyfagor\nSelect>>>')

        if operator == '1':
            result = add(a, b)
        elif operator == '2':
            result = sub(a, b)
        elif operator == '3':
            result = mult(a, b)
        elif operator == '4':
            result = div(a, b)
        elif operator == '5':
            result = pifagor(a, b)
        else:
            print('Invalid operator!')
            continue

        print(result)

# print(__name__)
if __name__ == '__main__':
    main()