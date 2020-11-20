from itertools import permutations

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# input_list = [1, 2, 3]

for var in permutations(input_list, 9):
    check = sum(var[:3])
    if (sum(var[3:6]) != check or sum(var[6:]) != check
            or sum([var[0], var[3], var[6]]) != check
            or sum([var[1], var[4], var[7]]) != check
            or sum([var[2], var[5], var[8]]) != check
            or sum([var[0], var[4], var[8]]) != check
            or sum([var[2], var[4], var[6]]) != check):
        continue
    print('*' * 10)
    print(var)
    print(check)

# (2, 9, 4, 7, 5, 3, 6, 1, 8)
# 15
# **********
# (4, 3, 8, 9, 5, 1, 2, 7, 6)
# 15
# **********
# (4, 9, 2, 3, 5, 7, 8, 1, 6)
# 15
# **********
# (6, 1, 8, 7, 5, 3, 2, 9, 4)
# 15
# **********
# (6, 7, 2, 1, 5, 9, 8, 3, 4)
# 15
# **********
# (8, 1, 6, 3, 5, 7, 4, 9, 2)
# 15
# **********
# (8, 3, 4, 1, 5, 9, 6, 7, 2)
# 15
