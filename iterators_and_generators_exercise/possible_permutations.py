from itertools import permutations


def possible_permutations(lst):
    for el in permutations(lst):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
