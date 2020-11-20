# from visualiser.visualiser import Visualiser as vs

# @vs(node_properties_kwargs={
#     "shape": "record",
#     "color": "#f57542",
#     "style": "filled",
#     "fillcolor": "grey"
# })
import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    fin_arr = []
    i1 = 0
    i2 = 0
    for pony in arr:
        if i1 < len(arr1) and i2 < len(arr2):
            if arr1[i1] < arr2[i2]:
                fin_arr.append(arr1[i1])
                i1 += 1
            elif arr2[i2] < arr1[i1]:
                fin_arr.append(arr2[i2])
                i2 += 1
        else:
            if i1 == len(arr1):
                fin_arr += arr2[i2:]
            else:
                fin_arr += arr1[i1:]
            break
    return fin_arr


test_array = [8, 1, 7, 4, 5]
# test_array = [8, 1, 7, 4, 5, 3, 9, 2, 6]
# test_array = [
#     20, 11, 8, 14, 19, 1, 12, 7, 18, 4, 13, 5, 3, 17, 9, 15, 2, 6, 16
# ]
print(merge_sort(test_array))
# vs.make_animation("fibonacci.gif", delay=2)