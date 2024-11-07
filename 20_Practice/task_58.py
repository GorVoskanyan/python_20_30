"""
В большинстве случаев год насчитывает 365 дней. Но на самом деле на
шей планете требуется чуть больше времени, чтобы полностью пройти по
своей орбите вокруг Солнца. В результате для компенсации этой разницы
был введен дополнительный день в феврале для особых годов, называе
мых високосными. Определить, високосный год или нет, можно, следуя
такому алгоритму:
если год делится на 400 без остатка, он високосный;
если год (из оставшихся) делится на 100 без остатка, он НЕ висо
косный;
если год (из оставшихся) делится на 4 без остатка, он високосный;
все остальные года не являются високосными.
Напишите программу, запрашивающую год у пользователя и выводя
щую сообщение о том, високосный ли он.
"""

year = int(input("Գրեք տարին։ "))
if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
    print("Նահանջ տարի է")
else:
    print("Ոչ նահանջ տարի")


