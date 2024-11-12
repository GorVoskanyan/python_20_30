import os
from fileinput import filename

current_directory = os.path.abspath('.')
filename = 'module_os.py'


file_abs_path = os.path.join(current_directory, filename)
print(file_abs_path)

# os.system('mkdir example')


for name in os.listdir('..'):
    abs_path = os.path.join(os.path.abspath('..'), name)
    if os.path.isdir(abs_path):
        print(abs_path, 'is directory')
    elif os.path.isfile(abs_path):
        print(abs_path, 'is file')
