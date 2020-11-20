test_array = [8, 1, 7, 4, 5, 3, 9, 2, 6]
# test_array = [9, 1, 3]
# ar1 = [1, 7, 4, 5]
# ar2 = [3, 6, 2, 9, 8]


def merge_sort(input_array):
    if len(input_array) > 1:
        mid = int(round(len(input_array) / 2))
        print(mid)
        ar1 = merge_sort(input_array[:mid])
        ar2 = merge_sort(input_array[mid:])
        fin = []
        i = 0
        j = 0
        for pony in input_array:
            if len(ar1) > i and len(ar2) > j:
                if ar1[i] < ar2[j]:
                    fin.append(ar1[i])
                    i += 1
                elif ar2[j] < ar1[i]:
                    fin.append(ar2[j])
                    j += 1
            else:
                if len(ar1) == i:
                    fin += ar2[j:]
                else:
                    fin += ar1[i:]
                break
        return fin
    else:
        return input_array


waka = merge_sort(test_array)
print('*' * 50)
print(waka)

# k arrays
# n elements in each array
# n(log(n))

# def merge_sort(input_array):
#     if len(input_array) > 1:
#         mid = round(len(input_array) / 2)
#         ar1 = merge_sort(input_array[:mid])
#         ar2 = merge_sort(input_array[mid:])
#         fin = []
#         i = 0
#         j = 0
#         for k in range(len(test_array)):
#             if len(ar1) > i and len(ar2) > j:
#                 if ar1[i] < ar2[j]:
#                     fin.append(ar1[i])
#                     i += 1
#                 elif ar2[j] < ar1[i]:
#                     fin.append(ar2[j])
#                     j += 1
#         print('*' * 5)
#         print(fin)
#         return fin
