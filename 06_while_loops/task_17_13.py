n = int(input())


while 0 < n < 10:
    if n < naxaverchin:
        print('No')
        break
    verchin = n % 10
    n //= 10
    naxaverchin = n % 10
    n //= 10
    if verchin >= naxaverchin:
        continue
    print('No')
    break
else:
    print('Yes')