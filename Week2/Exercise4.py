def my_bin(n):
    assert n >= 0

    return (my_bin(n // 2) + str(n % 2)) if n > 0 else ''


for i in range(256):
    print('{0:0>8}'.format(my_bin(i)))
