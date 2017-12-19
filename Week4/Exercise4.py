coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
A = []


def f(n):
    assert n <= 10000

    global coins
    global A

    last_coin_smaller_than_n = 0  # the last coin in coins list smaller than n
    # Fill answers list with n 1's for every coin smaller than n
    for i in range(len(coins)):
        if coins[i] <= n:
            last_coin_smaller_than_n = i

            # Append list with n 1's
            if len(A) <= i:
                A.append([1 for _ in range(n + 1)])
            # there is already a list for coins, but we have < 1's than na
            elif len(A[i]) < n + 1:
                for _ in range(n + 1 - len(A[i])):
                    A[i].append(1)

    # The answer is already in the list
    if len(A) > last_coin_smaller_than_n + 1 and len(A[last_coin_smaller_than_n + 1]) > n:
        return A[last_coin_smaller_than_n + 1][n]

    i = 0
    j = 0
    for i in range(last_coin_smaller_than_n + 1):
        # Skip i == 0 because A[0, n] = 1
        if i == 0:
            continue

        # Skip the first because A[i, 0] = 1
        for j in range(1, n + 1):
            if A[i][j] != 1:
                # This part of the variable is already calculated
                continue

            # j >= coins[i]: A[i, j] = A[i - 1][j] + A[i][j - coins[i]]
            if j >= coins[i]:
                A[i][j] = A[i - 1][j] + A[i][j - coins[i]]
            # j < coins[i]: A[i, j] = A[i - 1][j]
            else:
                A[i][j] = A[i - 1][j]

    return A[i][j]


print(f(100))
print(f(7))
print(f(10000))
