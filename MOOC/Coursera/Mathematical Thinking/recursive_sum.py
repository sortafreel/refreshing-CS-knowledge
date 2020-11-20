def recursive_sum(a, b):
    if b == 100:
        return 1/(a*b)
    return 1/(a*b)+recursive_sum(b, b+1)

print(recursive_sum(1, 2))