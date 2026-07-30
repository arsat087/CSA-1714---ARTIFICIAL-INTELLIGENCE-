from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
cities = list(range(1, n))

min_cost = float('inf')
best_path = []

for path in permutations(cities):
    current_cost = 0
    current = 0

    for city in path:
        current_cost += cost[current][city]
        current = city

    current_cost += cost[current][0]

    if current_cost < min_cost:
        min_cost = current_cost
        best_path = [0] + list(path) + [0]

print("Minimum Cost:", min_cost)
print("Best Path:", best_path)
