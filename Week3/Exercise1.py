def check(a, i): # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or
                # niet in dezelfde kolom
                i+n in [a[j]+j for j in range(n)] or
                # niet op dezelfde diagonaal
                i-n in [a[j]-j for j in range(n)])
                # niet op dezelfde diagonaal


def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X", end= " ")
            else:
                print("*", end= " ")
        print()
    print()


def rsearch(N, solutions, a = []):
    for i in range(N):
        if check(a, i):
            a.append(i)
            if len(a) == N:
                solutions.append(a[:])
            rsearch(N, solutions, a)
            del a[-1]  # verwijder laatste elemente
    return False

lst = []
t = 0
rsearch(8, lst)

for grid in lst:
    printQueens(grid)


print(len(lst))
