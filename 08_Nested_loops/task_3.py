"""
height: 5
5........5
54......45
543....345
5432..2345
5432112345
"""

height = int(input('height: '))

for row in range(height):
    for left_number in range(height, height - row - 1, -1):
        print(left_number, end='')

    points_count = (height - row - 1) * 2
    print(points_count * '.', end='')

    # for points_count in range(height - row - 1, -1, -1):
    #     print((points_count * 2) * '.', end='')
    #     break


    for right_number in range(height - row, height + 1):
        print(right_number, end='')

    print()

