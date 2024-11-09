open('example.txt', 'x')

file = open('example.txt', 'w')
file.write('hello world\n')
file.close()

file = open('example.txt', 'a', encoding='utf-8')
file.write('Բարև աշխարհ\n')
file.close()

file = open('example.txt', 'r', encoding='utf-8')
for line in file:
    print(line.rstrip())

all_lines = file.read(5)
print(all_lines)

first_line = file.readline()
second_line = file.readline(5)
print(first_line)
print(second_line)

all_lines_list = file.readlines()
print(all_lines_list)

data = ['third line\n', 'fourth line\n']
file = open('example.txt', 'a', encoding='utf-8')
file.writelines(data)
file.close()
