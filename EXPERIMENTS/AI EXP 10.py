
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

open_list = ['A']
closed_list = []
g = {'A': 0}
parent = {'A': None}

while open_list:
    current = open_list[0]

    for node in open_list:
        if g[node] + heuristic[node] < g[current] + heuristic[current]:
            current = node

    if current == 'G':
        break

    open_list.remove(current)
    closed_list.append(current)

    for neighbor, cost in graph[current]:
        new_cost = g[current] + cost

        if neighbor not in open_list and neighbor not in closed_list:
            open_list.append(neighbor)
            g[neighbor] = new_cost
            parent[neighbor] = current

        elif new_cost < g.get(neighbor, float('inf')):
            g[neighbor] = new_cost
            parent[neighbor] = current

            if neighbor in closed_list:
                closed_list.remove(neighbor)
                open_list.append(neighbor)

path = []
node = 'G'

while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()

print("Shortest Path:", path)
print("Total Cost:", g['G'])
