import sys
import platform

with open('os_info.txt', 'w', encoding='utf-8') as file:
    file.write(
        f"Sys verison: {sys.version}\n"
        f"Platform: {platform.uname()}"
    )

