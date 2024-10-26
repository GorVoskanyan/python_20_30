# N1
# print("Markos")
# print("Kotayq, Nairi, Qasax, Tumanyan street")


# N2
# name = input("Enter your name: ")
# print("Hi" + " " + name)

# N3
# print("Enter your numbers in metres!!!")
# lenght = float(input("Enter lenght :"))
# width = float(input("Enter widht: "))
# area = lenght * width
# print(lenght * width)
# a = "m/q"
# print(f"The are is: {area} {a}")

# N4
# print("Enter your numbers in funts!!!")
# lenght = float(input("Enter lenght :"))
# width = float(input("Enter widht: "))
# end = lenght * width / 43560
# print(f"your answer in arkas is: {end}")

# N5
# small_bottles = int(input("How many bottles do you bring under 1l or 1l?" ))
# big_bottles = int(input("How many bottles do you bring upper 1l?" ))
# sum1 = small_bottles * 0.1
# sum2 = big_bottles * 0.25
# sum = sum1 + sum2
# print(f"Total is: ${sum:.2f}")

# N6
# order = int(input("How much is your order? "))
# nalog = (order * 0.2)
# chayevo = order * 0.18
# sum1 = nalog + chayevo
# sum = order + sum1
# print(f"Nalog: {nalog:.2f}, \nChayevo: {chayevo:.2f}, \nNalog ev chayevo: {sum1:.2f}, \nobshi: {sum:.2f}")


# N7
# number = int(input("please give your number: "))
#
# sum = (number*(number+1))//2
# print(sum)

# N8
# suvenir = int(input("Enter your Suvenier count: "))
# bezdelushka = int(input("Enter your Beszdelushka count: "))
# total = suvenir * 75 + bezdelushka * 112
# print(f"Toltal is : {total} grams")

# N9
# first_deposit = int(input("Enter your first deposit: "))
# first_year = first_deposit * 1.04
# second_year = first_year * 1.04
# third_year = second_year * 1.04
#
# print(f"Your first year sum is: {first_year:.2f}, \nYour second year sum is: {second_year:.2f}, \nYour third year sum is: {third_year:.2f}")

# N10` հարց՝ ինչպես օգտագործել \n մի print ի մեջ
# from math import log10
#
# a = int(input("Enter your nunmber a: "))
# b = int(input("Enter your nunmber b: "))
# print(a + b, b - a, a * b, a / b, a // b, log10(a), a ** b, sep='\n')

# N11
# 1MPG(USA) = 235.215L/100KM(Canada)

# mpg = int(input("Miles per gallon: "))
# liter = mpg * 235.215
# print(f"{mpg} mpg = {liter} L/100km")

# N12

# from math import radians , acos, sin, cos
#
# t1 = radians(int(input("Enter your latitude t1 radians: ")))
# t2= radians(int(input("Enter your longitude t2 radians: ")))
# g1 = radians(int(input("Enter your latitude g1 radians: ")))
# g2= radians(int(input("Enter your longitude g2 radians: ")))
#
# distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))
# print(f"Distance is {distance: .3f}")
