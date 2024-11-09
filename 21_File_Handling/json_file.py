import json

# JSON: java script object notation

# with open('data.txt', 'w') as file:
#     data = {1: {1: {1: []}}}
#     file.write(str(data))

# with open('data.txt', encoding='utf-8') as file:
#     data = file.read()
#     data = dict(data)
#
# print(data)
# print(type(data))



# with open('data.json', 'w', encoding='utf-8') as json_file:
#     data = {1: {1: {1: []}}}
#     json.dump(data, json_file, indent=2)

# with open('data.json', encoding='utf-8') as json_file:
#     data = json.load(json_file)

# print(data)
# print(type(data))


data = {1: {1: {1: []}}}
json_string = json.dumps(data)
# print(type(json_string))
# print(json_string)

data_2 = json.loads(json_string)
print(data_2)
print(type(data_2))