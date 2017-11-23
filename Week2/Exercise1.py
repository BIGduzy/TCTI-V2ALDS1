def machtv3(a, n):
    assert n > 0

    x = 0
    m = 1
    while n > 0:
        x += 1
        # Even
        if n % 2 == 0:
            a *= a
            n //= 2
        #odd
        else:
            m *= a
            n -= 1

    return m, x

print(machtv3(2, 3)[0])
print(machtv3(3, 2)[0])
print(machtv3(5, 1)[0])
print(machtv3(1, 6)[0])
print(machtv3(2, 5)[0])

# Number of multiplications
print(machtv3(2, 10000)[1])
