import random


def quick_sort(a):
    if len(a) == 2:
        return [a[0], a[1]] if a[0] < a[1] else [a[1], a[0]]

    pivot = a[random.randint(0, len(a) - 1)]
    a.remove(pivot)  # Remove pivot from the list
    left = []
    right = []
    for el in a:
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

lst = [2, 3, 1, 66, 1, 4, 8, 2, 3]
print(quick_sort(lst))
