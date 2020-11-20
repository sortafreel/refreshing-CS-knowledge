import itertools

variations = 3
items = 4
it = list(range(variations)) * items
combinations = set(itertools.combinations(it, items))

for x in combinations:
    print(x)
print('***')
print(len(combinations))
