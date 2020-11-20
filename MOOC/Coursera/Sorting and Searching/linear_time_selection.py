def select_median(ar, med_pos):
    len_ar = len(ar)
    # Base case
    if len_ar == 1:
        return ar[0]
    # Pick random pivot (first)
    pivot, pivot_position = ar[0], 0
    # Pick starting position to sort
    s = pivot_position + 1
    # Partition array (to divide to right-larger and left-smaller parts)
    for n in range(s, len_ar):
        if ar[n] < pivot:
            if n > s:
                ar[n], ar[s] = ar[s], ar[n]
            s += 1
    # Put pivot between smaller/larger numbers
    ar[0], ar[s - 1] = ar[s - 1], ar[0]
    # If median is on the required position
    if med_pos == s - 1:
        return pivot
    # Pick part
    elif med_pos > s - 1:
        return select_median(ar[s:], med_pos - s)
    elif med_pos < s - 1:
        return select_median(ar[:s - 1], med_pos)


# test_array = [4, 1, 7, 6, 2, 0, 8, 5, 3, 9, 10]
test_array = [
    62, 28, 47, 69, 24, 75, 23, 14, 96, 22, 19, 13, 66, 59, 70, 21, 60, 65, 80,
    52, 55, 85, 58, 32, 39, 41, 98, 64, 34, 76, 89, 79, 40, 7, 16, 95, 88, 31,
    56, 94, 6, 78, 74, 82, 27, 48, 26, 73, 9, 44, 15, 72, 83, 11, 29, 54, 43,
    8, 33, 1, 38, 84, 87, 81, 35, 93, 3, 68, 0, 17, 67, 71, 12, 51, 4, 90, 37,
    46, 30, 25, 86, 5, 20, 97, 2, 63, 99, 36, 61, 50, 10, 42, 57, 77, 49, 92,
    53, 45, 91
]
# If I want to pick the median, it must be the middle element of the sorted array
# So, I need to find index where it must be
if len(test_array) % 2 == 0:
    # Removing 1 because Python starts with 0
    # So, for 4th element I want to get index 3
    test_median_position = len(test_array) / 2 - 1
else:
    test_median_position = len(test_array) // 2
print(select_median(test_array, test_median_position))