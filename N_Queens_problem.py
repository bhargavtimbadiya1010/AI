# Check whether a queen can be placed safely
'''
board[row] = col: Places a queen at the specified row and column.
is_safe(): Checks whether the queen shares a column or diagonal with an existing queen.
solve_nqueens(): Uses recursion to place queens row by row.
solutions.append(board[:]): Saves a copy of each valid solution.
board[row] = -1: Removes the queen when backtracking.
len(solutions): Counts the total number of valid arrangements.
'''
def is_safe(board, row, col):
    # Check all previously placed queens
    for i in range(row):
        # Check same column or same diagonal
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True


# Place queens row by row using backtracking
def solve_nqueens(board, row, n, solutions):
    # If all rows have queens, save the solution
    if row == n:
        solutions.append(board[:])
        return

    # Try placing a queen in each column
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            # Recursively solve the next row
            solve_nqueens(board, row + 1, n, solutions)

            # Remove the queen and try another column
            board[row] = -1


# Set the board size to 4
n = 4

# Initialize the board with all rows empty
board = [-1] * n

# Store all valid solutions
solutions = []

# Start solving from the first row (row 0)
solve_nqueens(board, 0, n, solutions)

# Display the total number of solutions
print(f"Total solutions for {n}-Queens: {len(solutions)}")

# Display each solution as column positions
for sol in solutions:
    print(sol)
