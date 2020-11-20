import time


def check_distance(a, b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i] - b[i])**2
    return distance**0.5


def check_closest_pair(pairs):
    closest_pair = None
    closest_distance = None
    processed_pairs = set()
    for pair_index, pair in enumerate(pairs):
        # Reduce cycle by one (already processed combinations)
        processed_pairs.add(pair)
        for second_pair_index, second_pair in enumerate(pairs):

            # Points with same x, y, but different index
            # if second_pair == pair and pair_index != second_pair_index:
            #     return pair, second_pair, 0

            # Search for the item in array will slow down the process a lot,
            # because need to search through the whole array every time

            # But, if replace array with dict - it'll be faster
            # because dicts use hashmaps to search for a key faster

            # Sets are even faster and eat less memory

            if second_pair in processed_pairs:
                continue
            pair_distance = check_distance(pair, second_pair)
            if not closest_pair or pair_distance < closest_distance:
                closest_pair = [pair, second_pair]
                closest_distance = pair_distance
    return closest_pair, closest_distance


start = time.time()
solution = check_closest_pair([(3, 0), (4, 3), (3, 3), (2, 3), (12, 5), (4, 2),
                               (2, 0)] * 100)
end = time.time()
print(end - start)
print(solution)

# Average time for basic solution
# 0.3110651969909668
# 0.3146030902862549
# 0.3287944793701172
# 0.3271150588989258
# 0.3125615119934082

# Average time for avoid checking already processed combinations
# 0.025591611862182617
# 0.025749921798706055
# 0.025547027587890625
# 0.025035619735717773
# 0.025571346282958984
