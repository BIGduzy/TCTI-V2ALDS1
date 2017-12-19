pascal = {
    0: {0: 1},
    1: {0: 1},
    2: {0: 1},
    3: {0: 1},
    4: {0: 1},
    5: {0: 1},
    6: {0: 1},
}


def B(n, k):
    global pascal

    if n in pascal and k in pascal[n]:
        return pascal[n][k]

    if k > n + 1:
        raise ValueError("k can not be > n + 1")

    if k == 0 or n == k:
        if n in pascal:
            pascal[n][k] = 1
        else:
            pascal[n] = {k: 1}
        return 1

    result = B(n - 1, k) + B(n - 1, k - 1)
    if n < len(pascal):
        pascal[n][k] = result
        return result

    pascal[n] = {k: result}
    return result

# 100,891,344,545,564,193,334,812,497,256
# print("{:,}".format(B(100, 50)))
print("{:,}".format(B(6, 4)))
print("{:,}".format(B(6, 3)))
print("{:,}".format(B(3, 1)))
print("{:,}".format(B(8, 1)))
print()

len_x = 0
len_y = 0
largest_num = 0
for key in pascal:
    if key > len_y:
        len_y = key

    for k in pascal[key]:
        if k > len_x:
            len_x = k
        tmp_len = len(str(pascal[key][k]))
        if tmp_len > largest_num:
            largest_num = tmp_len
start = 4

len_x += 1
len_y += 1


print(' ' * start, 'i |', end = ' ')
for i in range(len_x):
    print(i, end = ' ' * largest_num)
print(end = '\n')
print(' ' * start + ' ' * 4, '-' * len_x * largest_num + '-' * (3 * largest_num))


# TODO: still not working purrfect
for i in range(len_y):
    print('Rij ', i, '|', end = ' ')

    for j in range(len_x):
        if i in pascal:
            if j in pascal[i]:
                print(pascal[i][j], end = ' ' * largest_num)
                continue

        if i < j + 1:
            print(' ', end = ' ' * largest_num)
        else:
            print('-', end = ' ' * largest_num)

    print(end = '\n')
