n = int(input())

s = ''
hashvich = 0

while n:
    verchin_tvanshan = n % 10
    hashvich += verchin_tvanshan
    str_verchin = str(verchin_tvanshan)

    s = str_verchin + ' ' + s
    n //= 10

print(s)
print(hashvich)