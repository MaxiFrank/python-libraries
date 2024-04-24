Generating Random Integers:
- random.randint(a, b): Generates a random integer between a and b, inclusive.

Generating Random Floating-Point Numbers:
- random.random(): Generates a random float between 0 and 1.
- random.uniform(a, b): Generates a random float between a and b.

Choosing Random Elements from a Sequence:
- random.choice(sequence): Chooses a random element from a sequence.
- random.choices(sequence, k=n): Chooses n random elements from a sequence with replacement (sampling with replacement).
- random.sample(sequence, k=n): Chooses n random elements from a sequence without replacement (sampling without replacement).

Shuffling Sequences:
- random.shuffle(sequence): Shuffles the elements of a sequence in place.

Generating Randomness with Seeds:
- random.seed(): Initializes the random number generator with the current system time.
- random.seed(seed): Initializes the random number generator with a specified seed value.

Other Random Operations:
- random.getrandbits(k): Returns a Python integer with k random bits.
- random.randrange(start, stop[, step]): Returns a randomly selected element from the specified range.
