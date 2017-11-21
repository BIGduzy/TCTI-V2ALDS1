def print_prime():
    """
    Description
    Prints prime numbers below 1000
    """

    maxNumber = 1000
    primes = []
    not_prime = set()
    for i in range(2, maxNumber):
        if i in not_prime:
            continue

        for j in range(i * i, maxNumber, i):
            not_prime.add(j)
        primes.append(i)

    print(primes)

print_prime()
