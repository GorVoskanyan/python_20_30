goods = {
    'Լամպ': '12345',
    'Սեղան': '23456',
    'Դիվան': '34567',
    'Աթոռ': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product_name, product_code in goods.items():
    total_quantity = 0
    total_cost = 0
    for item in store[product_code]:
        total_quantity += item['quantity']
        total_cost += item['quantity'] * item['price']
    print(f"{product_name} - {total_quantity} հատ, ընդհանուր արժեքը՝ {total_cost} դրամ")
