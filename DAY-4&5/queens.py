def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]
    
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, col):
    # Recursive function to solve the N-Queens problem
    
    if col >= len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    
    return False

def print_board(board):
    # Function to print the chessboard with queens
    
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))

def main():
    n = 4
    board = [[0] * n for _ in range(n)]
    
    if solve_n_queens(board, 0):
        print("Solution Found:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()

