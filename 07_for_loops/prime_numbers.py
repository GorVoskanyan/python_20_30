num = int(input('Enter number: '))

for divider in range(2, num):
    if num % divider == 0:
        print(num, ':', divider, '=', num // divider)
        print(num, 'is not prime')
        break
else:
    print(num, 'is prime.')