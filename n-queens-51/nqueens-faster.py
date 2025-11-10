from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # columns already used
        cols = set()
        # diag1: r - c (top-left to bottom-right)
        diag1 = set()
        # diag2: r + c (top-right to bottom-left)
        diag2 = set()

        board = [["."] * n for _ in range(n)] # represents the n x n chessboard [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

        ans: List[List[str]] = [] # ans = [], to store the final board configurations

        def backtrack(r: int) -> None: # r is current row we are trying to place a queen in. Start from row 0 to n-1
            if r == n:
                ans.append(["".join(row) for row in board]) # concatenate each row into a string and add to ans
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # place
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                backtrack(r + 1)

                # remove
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return ans

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