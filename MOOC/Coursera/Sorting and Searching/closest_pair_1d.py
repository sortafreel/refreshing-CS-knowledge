import time
import random


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


def find_closest_pair_brute(sequence):
    closest_pair = None
    closest_distance = None
    for num in sequence:
        for second_num in sequence:
            if num == second_num:
                continue
            pair_distance = abs(num - second_num)
            if not closest_pair or pair_distance < closest_distance:
                closest_pair = [num, second_num]
                closest_distance = pair_distance
    return closest_pair, closest_distance


def find_closest_pair_brute_decrease(sequence):
    closest_pair = None
    closest_distance = None
    processed_nums = set()
    for num in sequence:
        # Reduce cycle by one (already processed combinations)
        processed_nums.add(num)
        for second_num in sequence:
            if second_num in processed_nums:
                continue
            pair_distance = abs(num - second_num)
            if not closest_pair or pair_distance < closest_distance:
                closest_pair = [num, second_num]
                closest_distance = pair_distance
    return closest_pair, closest_distance


def find_closest_pair_sort(sequence):
    sequence = merge_sort(sequence)
    closest_pair = None
    closest_distance = None
    for index, num in enumerate(sequence):
        if index == 0:
            continue
        prev = sequence[index - 1]
        distance = abs(prev - num)
        if index == 1 or distance < closest_distance:
            closest_pair = [prev, num]
            closest_distance = distance
    return closest_pair, closest_distance


n = 500000
sample = random.sample(range(0, n), round(n / 10))

start = time.time()
solution = find_closest_pair_brute(sample)
end = time.time()
print('***')
print('Brute')
print(end - start)
print(solution)

start = time.time()
solution = find_closest_pair_brute_decrease(sample)
end = time.time()
print('***')
print('Brute decrease')
print(end - start)
print(solution)

start = time.time()
solution = find_closest_pair_sort(sample)
end = time.time()
print('***')
print('Sort')
print(end - start)
print(solution)
