# student_info = ['Markos', 30, True]
# name = student_info[0]
# age = student_info[1]
# is_student = student_info[2]

# student_info = {
#     'name': 'Markos',
#     'age': 30,
#     'is_student': True
# }

# print(student_info['age'])

# iterate over dict
# for key in student_info:
#     print(key, '->', student_info[key])

# for key in student_info.keys():
#     print(key, '->', student_info[key])

# for value in student_info.values():
#     print(value)

# for item in student_info.items():
#     print(item)

# for key, value in student_info.items():
#     print(key, value)

# print('age' in student_info)
# print('Markos' in student_info.values())
# print(student_info)
# print(student_info.keys())
# print(list(student_info.values()))
# print(student_info.items())


# songs_data = {
#     'fragile': 2.55,
#     'yerazi im erkir hayreni': 4.44,
#     'hekiatn': 3.45,
#     'lost': 2.33
# }
#
# total_seconds = 0
# # for number in range(1, 3):
# while True:
#     song_name = input('Enter song name: ')
#     if not song_name:
#         break
#     song_duration = songs_data.get(song_name, 0.0)
#     minutes, seconds = str(song_duration).split('.')
#     total_seconds += int(seconds)
#     total_seconds += int(minutes) * 60
#
# minutes, seconds = total_seconds // 60, total_seconds % 60
# print(minutes, seconds, sep=':')

# student_info = {
#     'name': 'Markos',
#     'age': 30,
#     'is_student': True
# }

# deleted = student_info.pop('name')
# print(deleted)
# print(student_info)

# deleted_item = student_info.popitem()
# print(deleted_item)

# deleted_key, deleted_value = student_info.popitem()
# print(deleted_key, deleted_value)
# print(student_info)

# student_info.copy()
# student_info.clear()

# updated_student_info = {'languages': ['python', 'java'], 'age': 31}
# student_info.update(updated_student_info)
# print(student_info)

# student_names = ['Markos', 'Anna', 'Tigran', 'Gor']
# students_dict = dict.fromkeys(student_names, 'python')
# print(students_dict)

# student_info.setdefault('language', 'python')
# print(student_info)


# dictionary
dictionary = dict()

words_count = int(input('Enter words count: '))

for i in range(words_count):
    word = input('Enter word: ')
    synonym = input('Enter synonym: ')
    dictionary[word] = synonym

print(dictionary)

while True:
    word = input('Enter word: ')
    if not word:
        print('Bye-Bye.')
        break
    for key, value in dictionary.items():
        if word == key:
            synonym = value
            print(synonym)
            break
        elif word == value:
            synonym = key
            print(synonym)
            break
    else:
        print('Not found.')