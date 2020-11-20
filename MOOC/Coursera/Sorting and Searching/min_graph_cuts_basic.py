import random
from copy import deepcopy


def process_vertex(line):
    raw = line.split()
    return (raw[0], raw[1:])


# IMPORTANT: Undirected loop, names "tail"/"head" are personal preferences
def random_contraction(vertices):
    # Base case
    if len(vertices) <= 2:
        return vertices
    # Pick random vertex and random edge
    tail = random.choice(list(vertices.keys()))
    head = random.choice(vertices[tail])
    # Merging all edges into new contraction and removing head
    vertices[tail] += vertices[head]
    del vertices[head]
    # Removing self-loops
    vertices[tail] = [x for x in vertices[tail] if x != head and x != tail]
    # Go through all the vertices and update the link from head to tail
    # So all connections are still there
    for key, value in vertices.items():
        if key == tail:
            continue
        vertices[key] = [tail if x == head else x for x in value]
    # Go one level deeper :)
    return random_contraction(vertices)


with open('assets/kargerMinCut.txt', 'r') as f:
    # Processing and filtering vertices without edges
    test_vertices = {
        i: e
        for i, e in [process_vertex(x) for x in f.readlines()] if len(e) > 0
    }

min_cuts = []
for i in range(1000):
    cuts = random_contraction(deepcopy(test_vertices))
    key = [x for x in cuts.keys()][0]
    # # Base checks
    # # Only two keys
    # assert len(cuts) == 2
    # # All tails edges are the same
    # assert cuts[key].count(cuts[key][0]) == len(cuts[key])
    # # Head exists and has same number of connections
    # assert len(cuts[cuts[key][0]]) == len(cuts[key])
    # # And they're connected to tails
    # assert cuts[cuts[key][0]].count(key) == len(cuts[key])
    # If checks passed - save min cut (number of edges)
    min_cuts.append(len(cuts[key]))
print(min(min_cuts))
