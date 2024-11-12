with open('os_info.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    max_length_word = max(words, key=len)
    print(max_length_word)
