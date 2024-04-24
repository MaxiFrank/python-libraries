import random

# Generating Random Integers:
def random_integer():
    print(random_integer.__name__)
    # generate a random integer between a and b, inclusive
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10
    print(random.randint(1, 10))    # 1 <= x <= 10

# Generating Random Floating-Point Numbers:
def random_float():
    print(random_float.__name__)
    # to generate a random floating-point number between 0 and 1
    print(random.random())         # 0 <= x < 1
    # random.uniform(a, b): Generates a random float between a and b.
    print(random.uniform(1, 10))   # 1 <= x <= 10
    print(random.uniform(0, 1))   # 1 <= x <= 1

# Choosing Random Elements from a Sequence:
def random_choice():
    print(random_choice.__name__)
    #random.choice(sequence): Chooses a random element from a sequence.
    print(random.choice([1, 2, 3, 4, 5]))
    #random.choices(sequence, k=n): Chooses n random elements from a sequence with replacement (sampling with replacement)
    print(random.choices([1, 2, 3, 4, 5], k=3))  # k = 3
    print(random.choices([5], k=3))  # k = 3
    #random.sample(sequence, k=n): Chooses n random elements from a sequence without replacement (sampling without replacement).
    print(random.sample([1, 2, 3, 4, 5], k=3))  # without replacement

# Shuffling Sequences:
def random_shuffle():
    """
    random.shuffle(sequence): Shuffles the elements of a sequence in place.

    note it returns None and shuffles in place
    """

    print(random_shuffle.__name__)
    l = [1, 2, 3, 4, 5]
    random.shuffle(l)     
    print(l) # [1, 2, 3, 4, 5] == [5, 4, 3, 2, 1]


# Generating Randomness with Seeds:
def random_seed():
    print(random_seed.__name__)
    #random.seed(): Initializes the random number generator with the current system time.
    random.seed()
    print(random.random())
    # random.seed(seed): Initializes the random number generator with a specified seed value.
    random.seed(10)  # random.seed(10)
    print(random.random())
    print(random.random())
    print(random.random())
    print(random.random())
    random.seed(10)  # random.seed(10)
    # the next 4 numbers should look the same as the first 4 numbers because the random number generated is seeded with the same number.
    print(random.random())
    print(random.random())
    print(random.random())
    print(random.random())

# Other Random Operations:
def random_getrandbits():
    print(random_getrandbits.__name__)
    print(random.getrandbits(10))    # 0 <= x < 2**10
# - random.getrandbits(k): Returns a Python integer with k random bits.
def random_randrange():
    print(random_randrange.__name__)
    print(random.randrange(1, 10))    # 1 <= x < 10
# - random.randrange(start, stop[, step]): Returns a randomly selected element from the specified range.

if __name__ == "__main__":
    random_integer()
    random_float()
    random_choice()
    random_shuffle()
    random_seed()
    random_getrandbits()
    random_randrange()