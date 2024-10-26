# Ex2. Ask the user for a number 𝑛  and calculate the sum of all odd numbers from 1  to 𝑛.
# Ex3. Ask the user for a number 𝑛. Then, calculate and print the sum of all numbers from 1 to 𝑛.
# Ex4. Ask the user for a starting number. Calculate the sum of all numbers counting down to 1.
# Ex5. Ask the user for a positive integer. Calculate the sum of its digits (for example, for 123 , the sum would be 1+2+3=6).


# n= int(input('>>> '))
#
# odds_sum = 0
# all_sum = 0
# for number in range(1, n + 1):
#     print('Number:', number)
#     if number % 2 != 0:
#         odds_sum += number
#     all_sum += number

# gumar = sum(range(1, n + 1, 2))
# print(odds_sum)
# print(all_sum)


# n = int(input('>>> '))
#
# all_sum = 0
# for num in range(n, 0, -1):
#     print(num)
#     if num == 5:
#         break
#     all_sum += num
# print(all_sum)

# number = '123'
# _sum = 0
# for digit in number:
#     _sum += digit

# number = int(input('>>> '))
#
# _sum = 0
# while number != 0:
#     print(number)
#     _sum += number % 10
#     number //= 10
# print(_sum)