import time
import itertools as it


def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True


def find_solution(n):
    solutions = []
    for perm in it.permutations(range(n)):
        if is_solution(perm):
            solutions.append(perm)
        else:
            continue
    return solutions


# print(is_solution([1, 3, 0, 2]))
# print(is_solution([3, 1, 0, 2]))
start = time.time()
solutions = find_solution(10)
end = time.time()
print(end - start)
print('Solutions: {}'.format(len(solutions)))