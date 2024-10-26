# nested loops

# for row in range(6):
#     for column in range(6):
#         print(row + column, end='\t')
#     print()

length = int(input('Length: '))
height = int(input('Height: '))

for row in range(height):
    for col in range(length):
        if row == height // 2:
            print('-', end='')
        elif col == length // 2:
            print('|', end='')
        else:
            print(' ', end='')
    print()


