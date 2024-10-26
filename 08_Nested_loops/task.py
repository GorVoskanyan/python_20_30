# Ask the user for a positive integer. Reverse the digits of that integer.
# Then calculate and print the product of the reversed digits.
# (For example, if the user inputs 234, the reversed digits are 432, and the product would be 4 * 3 * 2 = 24.)


n = int(input('>>> '))
prod = 1

while n:
    last_digit = n % 10
    prod = prod * last_digit
    n = n // 10
    print(last_digit, end=' * ')
print('=', prod)