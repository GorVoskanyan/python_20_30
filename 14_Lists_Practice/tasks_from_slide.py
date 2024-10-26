""" Write a Python program to get the largest text from a list"""

# tveri_list = [1, 2, -3, 4, 5, 6, 7, 8]
# gumar = 0
# artadryal = 1
#
# for tiv in tveri_list:
#     gumar = gumar + tiv
#     artadryal = artadryal * tiv
#
# print(gumar)
# print(artadryal)

# import math
#
# print(math.prod(tveri_list))

# words = ['this', 'is', 'a', 'test', 'of', 'lesson', 'end']
# print(max(words, key=len))

# max_word_length = 0
# max_word = None

# for word in words:
#     if len(word) > max_word_length:
#         max_word_length = len(word)
#         max_word = word
#
# print(max_word_length, max_word)


from random import randint

numbers_list = [randint(-1000, 1000) for _ in range(randint(20, 30))]
max_number = numbers_list[0]
print(numbers_list)

for num in numbers_list[1:]:
    if num > max_number:
        max_number = num

print(max_number)
