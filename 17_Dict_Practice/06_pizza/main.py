# Մուտքագրեք պատվերների քանակը: 6
# Առաջին պատվեր: Իվանով — Պեպերոնի — 1
# Երկրորդ պատվեր: Պետրով — Դե-Լյուքս — 2
# Երրորդ պատվեր: Իվանով — Մսային — 3
# Չորրորդ պատվեր: Իվանով — Մեքսիկական — 2
# Հինգերորդ պատվեր: Իվանով — Պեպերոնի — 2
# Վեցերորդ պատվեր: Պետրով — Հետաքրքիր — 5

orders_count = int(input('Մուտքագրեք պատվերների քանակը: '))

for i in range(1, orders_count + 1):
    username, pizza_type, pizza_count = input(f'{i} պատվեր: ').split(' - ')
    print(username, pizza_type, pizza_count)
