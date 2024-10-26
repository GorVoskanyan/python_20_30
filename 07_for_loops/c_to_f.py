# Fahrenheit (°F) = (Celsius x 1.8) + 32

print('|  C   |   F  |')
print('-------------------')
# print(f"{'C':>5} {'|':>3} {'F':>5}")
# print('-'*17)
for celsius in range(0, 101, 10):
    fahrenheit = celsius * 1.8 + 32
    print('| ', celsius, '   |  ', fahrenheit, '  |')
    # print(f"|{celsius:>5} {'|':>3} {fahrenheit:>5}|")