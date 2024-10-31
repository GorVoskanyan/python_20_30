#Task 1
# def reverseLookup(dictionary: dict, value) -> list:
#     return [key for key, val in dictionary.items() if val == value]
# sample_dict = {
#     'a': 10,
#     'b': 20,
#     'c': 10,
#     'd': 30,
# }
# print("Key for Value 10:", reverseLookup(sample_dict, 10))
# print("key for value 20:", reverseLookup(sample_dict, 20))
# print("Key for value 50:", reverseLookup(sample_dict, 50))

#Task 2
# import random
#
# def roll_dice():
#     return random.randint(1, 6) + random.randint(1, 6)
#
# rolls_frequency = {i: 0 for i in range(2, 13)}
# num_simulations = 1000
#
# for _ in range(num_simulations):
#     result = roll_dice()
#     rolls_frequency[result] += 1
#
# theoretical_percentages = {
#     2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
#     7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
#     }
#Task 3
# def text_to_keys(text):
#     key_mapping = {
#         'A': '2', 'B': '22', 'C': '222',
#         'D': '3', 'E': '33', 'F': '333',
#         'G': '4', 'H': '44', 'I': '444',
#         'J': '5', 'K': '55', 'L': '555',
#         'M': '6', 'N': '66', 'O': '666',
#         'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
#         'T': '8', 'U': '88', 'V': '888',
#         'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
#         '1': '1', '.': '11', ',': '111', '?': '1111', '!': '11111', ':': '111111',
#         ' ': '0'
#     }
#
#
#     text = text.upper()
#
#
#     keypress_sequence = ''.join(key_mapping[char] for char in text if char in key_mapping)
#     return keypress_sequence
#
# user_input = input("Enter text to convert: ")
# result = text_to_keys(user_input)
# print("Sequence of keys:", result)
#
#Task 4
# morse_code = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
# }
#
# def text_to_morse(text):
#     text = text.upper()
#     morse_message = [morse_code[char] for char in text if char in morse_code]
#     return ' '.join(morse_message)
#
# user_input = input("input text to convert to morse code: ")
# result = text_to_morse(user_input)
# print("Your text in morse code:", result)