def is_even(p):
    count = 0
    # Bubble sort
    for pony in p:
        for i in range(len(p) - 1):
            if p[i + 1] < p[i]:
                count += 1
                p[i + 1], p[i] = p[i], p[i + 1]
    print(count)
    if count % 2 == 0:
        return True
    else:
        return False

print(is_even([0,3,2,4,5,6,7,1,9,8]))
