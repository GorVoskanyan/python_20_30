"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в  размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму оплаты такси.
В основной программе должен демонстрироваться результат вызова функции.
"""

def taximeter(distance_km):
    distance_m = distance_km * 1000
    base = 4
    price_per_140_m = 0.25
    total_price = distance_m / 140 * price_per_140_m + base
    return round(total_price, 2)

def main():
    distance = float(input('Enter distance: '))
    price = taximeter(distance)
    print(price, '$')


if __name__ == '__main__':
    main()
