"""
|--------------------------|
|                          |
|                          |
|                          |
|                          |
|                          |
|--------------------------|
"""
height = int(input('Height '))
length = int(input('Length '))

for row in range(height):
    for col in range(length):
        if col == 0 or col == length - 1:
            print('|', end='')
        elif row == 0 or row == height - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()