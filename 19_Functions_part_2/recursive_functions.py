# def print_hi(name):
#     print(f"Hi {name}")
#
# print_hi('Gor')

# factorial of 5
# 5! = 1 * 2 * 3 * 4 * 5
# 5! = 5 * 4 * 3 * 2 * 1

# n = 5
# factorial = 1
#
# while n > 0:
#     factorial *= n
#     n -= 1
#
# print(factorial)

# def factorial(n):
#     if n == 1:                          # base case
#         return 1
#     result = n * factorial(n-1)         # recursive case
#     return result
#
# res = factorial(5)
# print(res)


# def my_sum():
#     n = int(input('>>> '))
#     if n == 0:
#         return 0
#     return n + my_sum()
#
# _sum = my_sum()
# print(_sum)


# l = [1, 1, [1, [1, 1, 1, [1, [1, [1, [1]]]]]]]
# def unpack(collection):
#     # if type(collection[0]) == int:
#     #     ...
#     if not collection:
#         return []       # base case
#     elif isinstance(collection[0], int):
#         return [collection[0]] + unpack(collection[1:])
#     elif isinstance(collection[0], list):
#         return unpack(collection[0])

# res = unpack(collection=l)
# print(res)

# -----------------------------
# fibonacci recursive

# import sys
#
# sys.setrecursionlimit(2000)

# cache = dict()
#
# def fibonacci(n):
#     if n < 2:
#         return n
#     if n not in cache:
#         result = fibonacci(n - 1) + fibonacci(n - 2)
#         cache[n] = result
#
#     return cache[n]
#
# fibo = fibonacci(1000)
# print(fibo)

# ---------------------
# from functools import cache
#
# @cache
# def fibo(n):
#     return n if n < 2 else fibo(n-1) + fibo(n-2)
#
# res = fibo(40)
# print(res)

