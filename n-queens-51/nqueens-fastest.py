from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans: List[List[str]] = []
        row_placement = [-1] * n  # row_placement[r] = column where queen sits in row r

        def backtrack(r: int, cols: int, d1: int, d2: int) -> None:
            if r == n:
                # build board
                board = []
                for rr in range(n):
                    c = row_placement[rr]
                    board.append("." * c + "Q" + "." * (n - c - 1))
                ans.append(board)
                return

            # bits 1 where a column is free this row
            # cols holds used columns; d1 holds used \ diags; d2 holds used / diags
            available = ((1 << n) - 1) & ~(cols | d1 | d2)
            while available:
                # pick rightmost available bit
                bit = available & -available
                c = (bit.bit_length() - 1)  # column index
                row_placement[r] = c
                backtrack(r + 1,
                          cols | bit,
                          (d1 | bit) << 1,   # shift for next row’s \ diagonals
                          (d2 | bit) >> 1)   # shift for next row’s / diagonals
                available &= available - 1  # clear the bit

        backtrack(0, 0, 0, 0)
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