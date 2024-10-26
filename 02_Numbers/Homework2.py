# N13
# 1loonie(1$) , 1toonie(2$), 1$ = 100cent, we have 1,5,10,25 cents

# change = int(input("Enter your change: "))
#
# toonie = change // 200
# loonie = (change % 200) // 100
# cent_25 = (change % 100) // 25
# cent_10 = (change % 25) // 10
# cent_5 = (change % 25) % 10 // 5
# cent_1 = change % 5
#
# print(toonie, "- toonie")
# print(loonie, "- loonie")
# print(cent_25, "- 25cent")
# print(cent_10, "- 10cent")
# print(cent_5, "- 5cent")
# print(cent_1, "- 1cent")

# N14
# 1duym = 2.54sm, 1fut = 30.48sm

# fut = float(input("Enter fut: "))
# duym = float(input("Enter duym: "))
# santimetr = fut * 30.48 + duym * 2.54
#
# print(santimetr,"sm")


# N15, 1fut = 12duym, 1yard = 3fut, 1 mile = 5,280 feet

# fut = float(input("Enter fut: "))
# duym = fut * 12
# yard = fut / 3
# mile = fut / 5280
#
# print(F"Your entered {fut}fut = {duym: .3f}duym")
# print(F"Your entered {fut}fut = {yard: .3f}yard")
# print(F"Your entered {fut}fut = {mile: .3f}mile")


# N16
# from math import pi
# r = float(input("Enter radius in: "))
# area = pi * r ** 2
# volume = (4 / 3) * pi * r ** 3
#
# print(f"The area is: {area:.2f}")
# print(f"The volume is: {volume:.2f}")

# N17, 1Joul = 3.6*10^6 = 8.9cent

# water_mass = float(input("Enter water mess m: "))
# temperature = float(input("Enter water temperature T: "))
# c = 4.186
#
# q = water_mass * c * temperature
# kilowat = q / (3.6*10**6)
# money = kilowat * 8.9
# print(f"Total q is: {q:.2f}")
# print(f"Total KW is: {kilowat:.3f}kw/h")
# print(f"Total Money is: {money:.4f}cent")    # after coding try kofee 200gram and 60C

# N18
# from math import pi
# radius = float(input("Enter radius: "))
# high = float(input("Enter high: "))
# V = pi * radius ** 2 * high
# print(F"V = {V:.1f}m^3")

# N19
# from math import sqrt
# d = float(input("Enter metres: "))
# v_i = 0
# a = 9.8
#
# v_f = sqrt(v_i ** 2 + 2 * a * d)
# print(f"{v_f:.3f}")

# N20, V=12, P=20mln, T=C(20)+273.15

# R = 8.314
# P = float(input("Enter P: "))
# V = float(input("Enter V: "))
# T = float(input("Enter temperature in Celsius: "))
# T += 273.15
# n = (P * V) / (R * T)
# print(int(n))

# 21

# b = float(input("Enter MainLeigh: "))
# h = float(input("Enter high: "))
#
# area = (b * h) / 2
# print(f"With your MineLeigh {b} and high {h} the area is: {area}")

# N22,
# from math import sqrt
# print("Remember a+b>c")
# triangular_side1 = float(input("Enter triangular_side1: "))
# triangular_side2  = float(input("Enter triangular_side2: "))
# triangular_side3  = float(input("Enter triangular_side3: "))
#
# s = (triangular_side1 + triangular_side2 + triangular_side3) / 2
# area = sqrt(s * (s - triangular_side1) * (s - triangular_side2) * (s - triangular_side3))
#
# print(f"The ares is {area: .2f}")

# N23
# from math import pi , tan
#
# n = int(input("Enter count of side : "))
# s = float(input("Enter leigh:  "))
#
# area = (n * s ** 2) /(4 * tan(pi/n))
# print(f" The area is {area: .2f}")


# N24
# days = int(input("Enter Days: "))
# hours = int(input("Enter Hours: "))
# minutes = int(input("Enter Minutes: "))
# seconds = int(input("Enter Seconds: "))
#
# Sum_seconds = days * 24 * 60 * 60 + 60 * 60 + 60 + seconds
# print(Sum_seconds)

# N25
# UserSeconds = int(input("Enter Seconds: "))
#
# days = UserSeconds // (24 * 60 * 60)
# hours = UserSeconds % (24 * 60 * 60) // 3600
# minutes = UserSeconds % (24 * 60 * 60) % 60
# seconds = UserSeconds % 60
#
# print(f"Days {days}")
# print(f"{hours:02}:{minutes:02}:{seconds:02}")

