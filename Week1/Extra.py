def next_las_seq(x):
    count = 0
    last = x[0]
    sequence = []
    for i in x:
        if i == last:
            count += 1
        else:
            sequence.append(count)
            sequence.append(last)
            last = i
            count = 1

    sequence.append(count)
    sequence.append(last)

    return sequence

x = [3, 3, 4, 1, 1, 6, 6, 6, 1]
# x = [3, 3, 4, 1, 1, 6, 6, 6, 6]
n = next_las_seq(x)
print(n)
