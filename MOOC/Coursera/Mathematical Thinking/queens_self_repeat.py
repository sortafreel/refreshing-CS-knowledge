valid_solutions = []

def can_be_extended(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n):
    if len(perm) == n:
        valid_solutions.append(perm)

    for k in range(n):
        if k in perm:
            continue
        perm.append(k)
        if can_be_extended(perm):
            extend(perm, n)
        perm.pop()


extend([], 8)
print(len(valid_solutions))