import time
import itertools as it


def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if abs(i - j) == abs(perm[i] - perm[j]):
            return False
    return True

def find_solution_opt(n):
    perm = list(range(n))
    # solutions = []
    for i in range(n):
        variant_perm = perm[:]
        variant_perm.remove(i)
        result = find_solution_variant(variant_perm, [i])
        if result is not False:
            # solutions.append(result)
            return result
    # return solutions


def find_solution_variant(perm, solution):
    if len(perm) == 1:
        result = solution + perm
        if can_be_extended_to_solution(result):
            return result
        else:
            return False

    for i in perm:
        if abs(solution[-1] - i) != 1:
            variant_perm = perm[:]
            variant_perm.remove(i)
            variant_solution = solution[:]
            variant_solution.append(i)
            if not can_be_extended_to_solution(variant_solution):
                continue
            result = find_solution_variant(variant_perm, variant_solution)
            if result is not False:
                return result
    else:
        return False

tries = []
for i in range(1):
    start = time.time()
    solution = find_solution_opt(25)
    print(solution)
    end = time.time()
    tries.append(end-start)
print(sum(tries)/len(tries))