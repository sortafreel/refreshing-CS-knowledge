from itertools import product

dice_type = 6
dice = list(range(1, dice_type + 1))
number_of_dices = 4
number_of_occurences = 2
expected_value = dice[5]

# All possible combinations of dices
dices_combinations = list(product(dice, repeat=number_of_dices))

# print(dices_combinations)
# waka = [x[0] * x[1] for x in dices_combinations]
# print(waka)
# print(sum(waka))
# raise ()

# Number of throws that includes at least N of expected_value
valid_throws = [
    x for x in dices_combinations
    if x.count(expected_value) >= number_of_occurences
]

# Probability to get the expected outcome
occurences_probability = len(valid_throws) / len(dices_combinations)
print('All combinations: {}'.format(len(dices_combinations)))
print('Valid throws: {}'.format(len(valid_throws)))
print('Probability: {:.3%} / {:.5}'.format(occurences_probability,
                                           occurences_probability))
