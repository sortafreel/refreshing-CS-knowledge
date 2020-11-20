def merge_sort_and_count_split_inversions(input_array):
    if len(input_array) > 1:
        mid = int(round(len(input_array) / 2))
        ar1, ar1_count = merge_sort_and_count_split_inversions(
            input_array[:mid])
        ar2, ar2_count = merge_sort_and_count_split_inversions(
            input_array[mid:])
        fin = []
        i = 0
        j = 0
        count = ar1_count + ar2_count
        for pony in input_array:
            if len(ar1) > i and len(ar2) > j:
                if ar1[i] < ar2[j]:
                    fin.append(ar1[i])
                    i += 1
                elif ar2[j] < ar1[i]:
                    fin.append(ar2[j])
                    j += 1
                    count += len(ar1[i:])
            else:
                if len(ar1) == i:
                    fin += ar2[j:]
                else:
                    fin += ar1[i:]
                break
        return fin, count
    else:
        return input_array, 0


with open('assets/IntegerArray.txt', 'r') as f:
    test_array = [
        int(x.replace('\r', '').replace('\n', '')) for x in f.readlines()
    ]

waka, count = merge_sort_and_count_split_inversions(test_array)
print('*' * 50)
print(waka)
print(count)