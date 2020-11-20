test_array = [3, 1, 0, 7, 5, 3, 8, 9, 4, 1, 6, 0, 2]

pivot = test_array[0]
if test_array[1] < pivot:
    i = 2
else:
    i = 1

for n in range(i, len(test_array)):
    if test_array[n] <= pivot:
        if n > i:
            test_array[n], test_array[i] = test_array[i], test_array[n]
        i += 1

test_array[0], test_array[i - 1] = test_array[i - 1], test_array[0]

print(test_array)
