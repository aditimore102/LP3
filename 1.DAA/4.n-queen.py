def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

# Global counter
steps = 0

def is_safe(board, row, col, n):
    global steps
    steps += 1  # entering is_safe

    # Check column
    for i in range(row):
        steps += 1
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        steps += 1
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        steps += 1
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    global steps

    # Base case: all queens placed
    steps += 1
    if row >= n:
        return True
    
    # Try placing queen in each column
    for col in range(n):
        steps += 1  # checking next column
        if is_safe(board, row, col, n):
            board[row][col] = 1
            steps += 1  # queen placed

            if solve_nqueens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0
            steps += 1  # backtracking operation

    return False


def n_queens_with_first_queen(n, first_row, first_col):
    global steps
    steps = 0  # reset counter for each run

    board = [[0] * n for _ in range(n)]
    board[first_row][first_col] = 1
    steps += 1  # first queen placed manually

    if solve_nqueens(board, first_row + 1, n):
        print("\n✅ Solution found:")
        print_board(board)
    else:
        print("\n❌ No solution exists for this configuration.")

    print(f"Total steps required: {steps}")


# --- Main Section ---
n = int(input("Enter the size of the chessboard (n): "))
first_row = int(input("Enter the row index of the first queen (0 to n-1): "))
first_col = int(input("Enter the column index of the first queen (0 to n-1): "))

if 0 <= first_row < n and 0 <= first_col < n:
    n_queens_with_first_queen(n, first_row, first_col)
else:
    print("Invalid position for the first queen.")

#Theory
N-Queens Problem — Theory
🔹 Problem Definition

The N-Queens problem is a classic backtracking algorithm problem.
It asks:

How can we place N queens on an N × N chessboard so that no two queens attack each other?

A queen can attack another piece if it lies:

In the same row

In the same column

Or on the same diagonal

Time complexity -O(N×N!)
Space complexity - O(N^2)

Graph - chess board size vs step requried