#!/usr/bin/python3
import sys

def print_solution(board):
    """Print the solution in the required format."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, col, n):
    """Solve the N queens problem using backtracking."""
    if col >= n:
        print_solution(board)
        return True
    
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n) or res
            board[i][col] = 0
    
    return res

def nqueens(N):
    """Set up the board and start solving the problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens(board, 0, N):
        print("No solution found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
