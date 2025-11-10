
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # We need sets to keep track of columns and diagonals that are occupied.
        # This allows for an O(1) check to see if a square is under attack.
        occupied_cols = set()
        # For positive diagonals (top-left to bottom-right), (row - col) is constant.
        occupied_pos_diagonals = set() 
        # For negative diagonals (top-right to bottom-left), (row + col) is constant.
        occupied_neg_diagonals = set()

        # This will store all the valid board configurations.
        result = []
        
        # 'board' will store the column index of the queen for each row.
        # For example, board[0] = 1 means the queen in row 0 is at column 1.
        board = [-1] * n

        def backtrack(row):
            # Base case: If we have placed a queen in every row (from 0 to n-1),
            # we have found a valid solution.
            if row == n:
                # Format the board into the required List[List[str]] format.
                formatted_board = []
                for r in range(n):
                    row_str = "".join(["Q" if board[r] == c else "." for c in range(n)])
                    formatted_board.append(row_str)
                result.append(formatted_board)
                return

            # Recursive step: Try to place a queen in the current row.
            for col in range(n):
                # Check if the current square (row, col) is under attack.
                if (col in occupied_cols or 
                    (row - col) in occupied_pos_diagonals or 
                    (row + col) in occupied_neg_diagonals):
                    continue # This square is not safe, try the next column.

                # --- Make a choice ---
                # Place the queen at (row, col).
                board[row] = col
                occupied_cols.add(col)
                occupied_pos_diagonals.add(row - col)
                occupied_neg_diagonals.add(row + col)

                # --- Recurse ---
                # Move to the next row.
                backtrack(row + 1)

                # --- Backtrack (Undo the choice) ---
                # Remove the queen from (row, col) to explore other possibilities.
                board[row] = -1
                occupied_cols.remove(col)
                occupied_pos_diagonals.remove(row - col)
                occupied_neg_diagonals.remove(row + col)

        # Start the backtracking process from the first row (row 0).
        backtrack(0)
        return result

if __name__ == '__main__':
    # Example Usage:
    solver = Solution()
    n = 4
    solutions = solver.solveNQueens(n)
    print(f"Found {len(solutions)} solutions for n = {n}:")
    for i, solution in enumerate(solutions):
        print(f"--- Solution {i+1} ---")
        for row in solution:
            print(row)
