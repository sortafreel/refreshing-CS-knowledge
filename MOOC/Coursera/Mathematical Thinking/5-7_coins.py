# Find the biggest number that can't be paid
# for i in range(1, 100):
#     if any([( ((i - 7*x) > 0 and (i - 7*x) % 5 == 0) or ((i - 7*x) == 0) or ((i - 5*x) == 0)) for x in range(1, 100)]):
#         continue
#     else:
#         print(i)


def change(amount):
    if amount % 7 == 0:
        return [7]*int(amount/7)
    elif amount % 5 == 0:
        return [5]*int(amount/5)
    else:
        for n in range(200):
            mid = amount-(7*n)
            if mid > 0 and mid % 5 == 0:
                return [7]*n + [5]*int(mid/5)


for i in range(24, 50):
    print('*'*50)
    print(i)
    print(change(i))
