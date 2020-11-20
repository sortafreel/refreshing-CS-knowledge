# How many connections point can have (if n points):
# n-1 max

# Total number of connections:
# n-1 ... n-(n-1) = 45 for n = 10

# One connection connects 2 points
# So one poing could have 9 connections max:
# 45*2/10 = 9 max for n = 10

# Number of odd points must be even
# Every time we add segment, the number of odd points
# either increases by 2, or decreases by 2
# If we connect 2 empty points - both of them are odd
# If we connect 1 more point - we still have 2 odd points, because point in the middle is even now
# If we connect 1 more point between 1st and 3rd - all the points are even now, etc.

# If we connect all 9 points between each other up to 4
# There's 0 odd points (odd number of neighbors)
# So it's fine, because number of odd points is even ALWAYS

# If we connect all 9 points between each other up to 5
# There's 9 odd points (all points have 5 neighbors)
# So, it's impossible, because number of odd points must be ALWAYS even


points = 10

def count_connections(n):
    if n == 1:
        return 0
    return n-1 + count_connections(n-1)

print(count_connections(points))