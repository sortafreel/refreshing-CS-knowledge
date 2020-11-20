# def could_be_moved(tower, circle):
#     if len(tower) == 0 or tower[-1] > circle:
#         return True
#     else:
#         return False

# towers = [[3, 2, 1], [], []]

# # while towers[1] != [3, 2, 1] or towers[2] != [3, 2, 1]:
# for x in range(10):
#     for index, circle in enumerate([x[-1] if len(x) else None for x in towers]):
#         if not circle:
#             continue
#         for tower_index, tower in enumerate(towers):
#             if tower_index == index:
#                 continue
#             elif could_be_moved(tower, circle):
#                 towers[index].pop()
#                 towers[tower_index].append(circle)
#                 print(towers)
#                 break

# Question 1
# The number of moves required to solve the Hanoi Towers puzzle for n=1n=1 and n=2n=2 discs is equal to 1 and 3,
# respectively. Implement the recursive solution for the Hanoi Towers (described in the lectures)
# and count the number of moves for n=6n=6 discs.
def calc_moves(n):
    if n == 1:
        return 1
    return n + sum([calc_moves(x) for x in range(n)])
print(calc_moves(6))