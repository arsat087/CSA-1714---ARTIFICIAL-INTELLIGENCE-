goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

def display(state):
    for row in state:
        print(row)
    print()

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state):
    x, y = find_blank(state)

    if x < 2:
        new = [row[:] for row in state]
        new[x][y], new[x + 1][y] = new[x + 1][y], new[x][y]
        return new

    elif y < 2:
        new = [row[:] for row in state]
        new[x][y], new[x][y + 1] = new[x][y + 1], new[x][y]
        return new

    return state

print("Enter the initial state (use 0 for blank):")
state = []

for i in range(3):
    row = list(map(int, input().split()))
    state.append(row)

print("\nInitial State:")
display(state)

while state != goal:
    state = move(state)
    display(state)

print("Goal State Reached!")
