from math import ceil


# def find_unknown_integer_steps(n, step, it):
#     if step >= n-1:
#         return step
#     step += ceil(n/(2**it))
#     print('Step: {}'.format(step))
#     it += 1
#     return n - find_unknown_integer_steps(n, step, it)


def find_steps(n, total):
    print(total-n)
    if n <= 1:
        return
    return find_steps(n-ceil(n/2), total)


# print(find_unknown_integer_steps(127, 0, 1))
find_steps(2097151, 2097151)


# ceil(127/2) + ceil((127−64)/2) + ceil((127−96)/2) + ceil((127−112)/2) + ceil((127−120)/2) + ceil((127−124)/2)
