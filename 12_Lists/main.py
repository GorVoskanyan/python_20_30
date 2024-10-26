# numbers_list = [1, 2, 3, 4, 5]
# print(numbers_list)

# first = numbers_list[0]
# last = numbers_list[-1]

# print(first)
# print(last)


# immutable vs mutable
# s = 'abc'
# l = ['a', 'b', 'c']

# s[0] = 'x'    # TypeError
# l[0] = 'x'
# print(l)


# garbage collector
# x = 'abc'
# print(id(x))
# y = x
# print(id(y))

#   type            str
#   value           abc
#   id              140720241275720
#   reference count 0

# y = 'a'
# x = 'b'



# iterate ove lists

# numbers_list = [10, 20, 30, 40, 50]

# for number in numbers_list:
#     print(number)

# s = 'internationalization'
# length_of_string = len(s)
# print(length_of_string)

# length_of_list = len(numbers_list)
# print(length_of_list)

# for index in range(length_of_list):
#     print(index, '->', numbers_list[index])

# for index, elem in enumerate(numbers_list):
#     print(index, elem)


# numbers_list = [1, 10, 31, 42, 2]
# gumar = 0
# qanak = 0

# qanak = len(numbers_list)
# gumar = sum(numbers_list)

# minimum = numbers_list[0]
# maximum = numbers_list[0]

# for number in numbers_list:
    # gumar += number
    # qanak += 1

    # if number > maximum:
    #     maximum = number
    # elif number < minimum:
    #     minimum = number

# mijin = gumar / qanak
# print(gumar)
# print(qanak)
# print(mijin)

# minimum = min(numbers_list)
# maximum = max(numbers_list)
#
# print(minimum)
# print(maximum)


# nested lists

songs = [
    ['Fragile', 2.00],
    ['Eraz im erkir hayreni', 3.45],
    ['Hekiatn', 4.55]
]

# for elem in songs:
#     print(elem)
#     for sub_elem in elem:
#         print(sub_elem)

# print(songs[-1][-1])
# print(len(songs))

# song_name = input('Enter song name: ')
#
# for song_info in songs:
#     # print(song_info)
#     # if song_name == song_info[0]:
#     if song_name in song_info:
#         print(song_info[1], 'minutes')
#         break
# else:
#     print('Nman erg chunenq')



# indexing, sliceing
# s = 'abcdefg'
# l = list(s)
# print(l, type(l))

# print(l[::2])
# print(l[1::2])

# print(l[0])
# print(l[-1])

# print(l[:4])

# print(l[-4:-2])  # -> de
# print(l[3:5])  # -> de

# print(l[3:4])
# print(l[3])

# print(l[::-1])


# list methods
# adding in list
# l = []
# l = l + [1]
# l += [2]

# l.append([3])
# l.extend([3])
# l.extend([3, 4, 5, 6])
# l.append([3, 4, 5, 6])
# l.extend('abcdefg')

# l.insert(0, -1)
# print(l)


# remove
# l.append('a')
# l.remove('a')
# l.clear()
# print(l)
# deleted = l.pop(1)
# print(deleted)


# count, index
# l = ['a', 'b', 'c', 'e', 'a', 'a']
# a_count = l.count('a')
# a_index = l.index('a', 2, 10000)
# print(a_index)

# reverse, sort
# l = ['c', 'a', 'A', 'b', 'B']
# l.reverse()
# l.sort(key=str.lower, reverse=True)
# print(l)
# sorted_l = sorted(l)
# print(l)
# print(sorted_l)

# l = [1, 'a', []]
# l.sort()    # TypeError


# copy
# import copy
# l = ['a', 'b', 'c', ['a', 'b', 'c']]
# l_copy = l.copy()
# l_copy = l[:]

# l_copy = copy.deepcopy(l)

# print(id(l))
# print(id(l_copy))

# l_copy[-1][-1] = 'w'
# print(l_copy)
# print(l)
