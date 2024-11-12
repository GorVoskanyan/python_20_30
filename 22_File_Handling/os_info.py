import sys
import platform
import os

username = input('Enter your name: ')
os.system(f'mkdir {username}')
file_path = os.path.join(os.path.abspath('.'), username)
file_name = 'os_info.txt'
abs_path = os.path.join(file_path, file_name)

with open(abs_path, 'w', encoding='utf-8') as file:
    file.write(
        f"Sys verison: {sys.version}\n"
        f"Platform: {platform.uname()}"
    )


print(sys.getsizeof(__name__))