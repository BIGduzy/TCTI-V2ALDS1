import random

hashes = dict()
i = 0
while True:
    i += 1
    number = random.random()  # get random
    hashed_number = hash(number)
    if hashed_number in hashes and hashes[hashed_number] != number:
        print("Woa! hashed ", number, " equals ", hashes[hashed_number])
        print("Found in: ", i, " tries")
        break

    if i == 30000000:
        print("could not find")
        break

    if i % 1000000 == 0:
        print("Still searching!", "{:,}".format(i))
    hashes[hashed_number] = number
