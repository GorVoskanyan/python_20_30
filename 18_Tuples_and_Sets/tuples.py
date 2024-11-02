# t = 1, 2, 3
# t = (1, 2, 3, 1, 1)

# print(t[0])
# print(type(t))

# print(t.count(1))
# print(t.index(1, 2, 20))

# t[0] = 'a'  # TypeError

# single = (1, )
# print(type(single))

# coordinates = (0, 1)
# print(coordinates)

# my_students_list = [('Artyom', 20), ('Markos', 30), ('Tigran', 22)]
# students_dict = dict(my_students_list)
# print(my_students_list)
# print(type(my_students_list))

# print(students_dict)
# for student_name, student_age in my_students_list:
#     print(student_name, '->', student_age)


# unpacking
# a = b = c = 1
# *a, b, c = 1, 2, 3, 4, 5
# print(a)
# print(b)
# print(c)

# def func(t):
#     for elem in t:
#         print(elem)
#
# func((1, 2, 3))


# def calculator(data):
#     minimum = min(data)
#     maximum = max(data)
#     average = sum(data) / len(data)
#     return minimum, maximum, average

# res = calculator([1, 2, 3, 4, 5])
# print(type(res))
# print(res)

# minimum, maximum, average = calculator([1, 2, 3, 4, 5])
# print(minimum)
# print(maximum)
# print(average)


# names = ['Artyom', 'Markos', 'Tigran']
# ages = [20, 30, 22]

# data = zip(names, ages)
# print(data)
# for item in data:
#     print(item)

# data_list = list(data)
# print(data_list)

# data_dict = dict(data)
# print(data_dict)
# print(data_dict.items())