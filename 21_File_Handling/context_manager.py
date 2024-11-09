with open('example.txt', 'r', encoding='utf-8') as file:
    print(''.join(file.readlines()))
    file.seek(0)
    print(file.read())

print(file.closed)