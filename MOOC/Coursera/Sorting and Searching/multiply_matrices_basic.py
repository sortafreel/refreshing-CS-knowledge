from pprint import pprint


def increase_matrix_size(matrix, n):
    return [x * n for x in matrix] * n


a = [[1, 3, 2],
     [4, 7, 9],
     [3, 5, 2]]
a = increase_matrix_size(a, 10)
# pprint(a)

b = [[2, 5, 4],
     [6, 9, 1],
     [3, 2, 8]]
b = increase_matrix_size(b, 10)
# pprint(b)

c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
c = increase_matrix_size(c, 10)
# pprint(c)

# O(n^3) - cubic, because of 3 nested for loops
for row_index in range(len(a)):
    for column_index in range(len(b)):
        for num_index in (range(len(a[row_index]))):
            c[row_index][column_index] += a[row_index][num_index] * \
                b[num_index][column_index]
pprint(c)
