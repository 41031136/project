import numpy as np
from itertools import permutations

# Distance matrix (using numpy)
matrix = np.array([ [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


def tsp_brute_force(matrix):
    n = matrix.shape[0]  # Get the size of the matrix (number of cities)
    nodes = list(range(n))  # Set of nodes
    min_cost = np.inf       # Initialize minimum cost to infinity
    best_path = None


    for perm in permutations(nodes):
        cost = 0
        for i in range(n - 1):
            cost += matrix[perm[i], perm[i + 1]]
        cost += matrix[perm[-1], perm[0]]  # Cost to return to the starting point

        # If a smaller cost is found, update the minimum cost and best path
        if cost < min_cost:
            min_cost = cost
            best_path = perm

    return best_path, min_cost

# Find the shortest path
shortest_path, min_cost = tsp_brute_force(matrix)
print("Shortest path:", shortest_path, "Total cost:", min_cost)
