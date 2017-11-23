def is_sorted(a):
    i = 0
    while i < len(a) - 1 and a[i] <= a[i + 1]:
        i += 1

    return i == len(a) - 1


def quick_sort(a):
    def sorter(a):
        if len(a) == 2:
            return [a[0], a[1]] if a[0] < a[1] else [a[1], a[0]]

        result = quick_sort(a[1:])

        return [a[0]] + result if result[0] >= a[0] else result + [a[0]]

    while not is_sorted(a):
        a = sorter(a)
    return a

lst = [2, 3, 1, 66, 1, 4, 8, 2, 3]
print(quick_sort(lst))
