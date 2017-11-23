import random


def random_experiment():
    """
    Description
    prints percentage of kiddos with same birthday with random-experiment
    """
    sample_size = 10000
    number_of_same = 0
    for i in range(sample_size):
        kiddos = [random.randint(1, 365) for day in range(23)]

        if len(kiddos) > len(set(kiddos)):
            number_of_same += 1

    print(number_of_same / sample_size * 100)


random_experiment()
