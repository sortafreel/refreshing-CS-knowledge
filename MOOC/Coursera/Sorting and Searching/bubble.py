def bubble_sort(arr):
    for pony in arr:
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
    
    return arr


test_array = [8, 1, 7, 4, 5, 3, 9, 2, 6]
print(bubble_sort(test_array))
