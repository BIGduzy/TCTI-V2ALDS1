import random
x = 0
y = 0


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def quick_sort(a, low = 0, high = -1):
    global x

    if high == -1:
        high = len(a) - 1
    if low < high:
        swap(a, low, random.randint(low, high))
        m = low
        for j in range(low + 1, high+1):
            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
            x += 1
        swap(a, low, m)
        if m > 0:
            quick_sort(a, low, m-1)
        quick_sort(a, m + 1, high)


def bad_quick_sort(a, low = 0, high = -1):
    global y

    if high == -1:
        high = len(a) - 1
    if low < high:
        tmp = a[low: high+1]
        swap(a, low, low + tmp.index(min(tmp)))
        m = low
        for j in range(low + 1, high+1):
            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
            y += 1
        swap(a, low, m)
        if m > 0:
            bad_quick_sort(a, low, m-1)
        bad_quick_sort(a, m + 1, high)


a = [random.randint(0, 44) for _ in range(500)]
quick_sort(a)
print(x)
print(a)

b = [random.randint(0, 44) for _ in range(500)]  # can't do 10'000 because stack size
bad_quick_sort(b)
print(y)
print(b)
