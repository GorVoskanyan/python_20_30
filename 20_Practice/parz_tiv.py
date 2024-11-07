
# number = int(input())
# try:
#     for i in range(2, int(number ** 0.5) +1):
#         if number % i == 0:
#             print("parz chi")
#             break
#     else:
#         print("parz")
# except TypeError:
#     print("Խնդրում ենք նշել դրական թիվ")


number = int(input())

for i in range(2, int(number ** 0.5) +1):
    if number % i == 0:
        print("parz chi")
        break
else:
    print("parz")




