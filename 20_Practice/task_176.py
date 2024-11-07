"""
Напишите программу, которая будет запрашивать слово у пользовате
ля и отображать его на экране в виде шифра из соответствующих слов,
обозначающих буквы исходного текста. Например, если пользователь
введет слово Hello, на экране должна быть отображена следующая по
следовательность слов: Hotel Echo Lima Lima Oscar. Для решения этой за
дачи вам предстоит использовать рекурсивную функцию, а не циклы.
При этом все небуквенные символы, введенные пользователем, можно
игнорировать.
"""

data = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
    'I': 'India', 'J': 'juliet', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
    'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
    'Y': 'Yankee', 'Z': 'Zulu'
}

def encode_nato(word):
    if word == '':
        return ''
    word = word.upper()
    char = word[0]
    word = word[1:]
    if not char.isalpha():
        return encode_nato(word)
    return data[char] + ' ' + encode_nato(word)


def main():
    while True:
        word = input('Enter your word to spell')
        if word.isalpha():
            result = encode_nato(word)
            print(result)
            break


if __name__ == '__main__':
    main()