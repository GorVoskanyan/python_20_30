text = input('Enter text: ')

# dict comprehension
# histogram = {char: text.count(char) for char in text}
histogram = dict()
for char in text:
    histogram[char] = text.count(char)

print(histogram)
inverted = dict()

for key, value in histogram.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]
    print(inverted)
# print(inverted)

