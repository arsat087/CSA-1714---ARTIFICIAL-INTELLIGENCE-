def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col):
    if col == 8:
        return True

    for row in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1):
                return True

            board[row][col] = 0

    return False

board = [[0 for i in range(8)] for j in range(8)]

if solve(board, 0):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")
