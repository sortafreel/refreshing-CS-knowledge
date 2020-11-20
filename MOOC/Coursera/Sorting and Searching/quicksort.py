def pick_pivot(ar):
    pivots = []
    # Add first pivot
    pivot_position = 0
    pivots.append((pivot_position, ar[pivot_position]))
    # Add middle pivot
    if len(ar) % 2 == 0:
        pivot_position = len(ar) // 2 - 1
    else:
        pivot_position = len(ar) // 2
    pivots.append((pivot_position, ar[pivot_position]))
    # Add last pivot
    pivot_position = len(ar) - 1
    pivots.append((pivot_position, ar[pivot_position]))
    # Pick median pivot
    if ((pivots[1][1] <= pivots[0][1] <= pivots[2][1])
            or (pivots[2][1] <= pivots[0][1] <= pivots[1][1])):
        return pivots[0]
    if ((pivots[0][1] <= pivots[1][1] <= pivots[2][1])
            or (pivots[2][1] <= pivots[1][1] <= pivots[0][1])):
        return pivots[1]
    if ((pivots[0][1] <= pivots[2][1] <= pivots[1][1])
            or (pivots[1][1] <= pivots[2][1] <= pivots[0][1])):
        return pivots[2]


def quicksort(ar, use_last=False):
    # Base case
    if len(ar) <= 1:
        return ar
    if use_last:
        pivot_position = len(ar) - 1
        pivot = ar[pivot_position]
    else:
        pivot_position, pivot = pick_pivot(ar)
    # Swap with the first element
    ar[pivot_position], ar[0] = ar[0], ar[pivot_position]
    # Sort array
    i = 1
    for n in range(i, len(ar)):
        if ar[n] < pivot:
            if n > i:
                ar[n], ar[i] = ar[i], ar[n]
            i += 1
    # Put pivot in the middle
    ar[0], ar[i - 1] = ar[i - 1], ar[0]
    # Sort arrays right and left of the pivot recursively
    ar[:i - 1] = quicksort(ar[:i - 1], use_last)
    ar[i:] = quicksort(ar[i:], use_last)
    # Return sorted array
    return ar


with open('assets/QuickSort.txt', 'r') as f:
    test_array = [int(x) for x in f.readlines() if x]
print(quicksort(test_array, use_last=True))
