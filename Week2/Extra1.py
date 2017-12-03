import random


def quick_sort(a):
    if len(a) == 2:
        return [a[0], a[1]] if a[0] < a[1] else [a[1], a[0]]

    pivot = a[random.randint(0, len(a) - 1)]
    tmp = a[:]
    tmp.remove(pivot)  # Remove pivot from the list
    left = []
    right = []
    for el in tmp:
        if el <= pivot:
            left.append(el)
        else:
            right.append(el)

    if left and right:
        return quick_sort(left) + [pivot] + quick_sort(right)
    elif left:
        return quick_sort(left) + [pivot]
    elif right:
        return [pivot] + quick_sort(right)
    else:
        return [pivot]


def quick_sort2(a):
    if len(a) > 1:
        pivot = a[random.randint(0, len(a) - 1)]
        tmp = a[:]
        tmp.remove(pivot)
        left = []
        right = []
        for el in tmp:
            if el <= pivot:
                left.append(el)
            else:
                right.append(el)

        if left:
            quick_sort2(left)
        if right:
            quick_sort2(right)

        a[:len(left)] = left
        a[len(left)] = pivot
        a[len(left) + 1:] = right

lst = [2, 3, 1, 66, 1, 4, 8, 2, 3]

print(quick_sort(lst))
quick_sort2(lst)
print(lst)
