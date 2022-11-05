from itertools import permutations


def possible_permutations(seq):
    for permutation in permutations(seq):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
