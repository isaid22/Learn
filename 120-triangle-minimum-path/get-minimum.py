from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Number of rows
        n = len(triangle)
        # 1D DP initialized with the last row
        dp = triangle[-1][:]  # copy to avoid modifying input
        
        # Process from second-last row up to the top (row 0, but python slicing is exclusive, so -1), step -1 going upwards.
        for i in range(n - 2, -1, -1): 
            for j in range(i + 1):  # row i has i+1 elements. j starts from 0 to i; all elements accounted for.
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        return dp[0] # this is the end, top row.


if __name__ == '__main__':
    # Simple runner with the provided examples
    solver = Solution()

    # Example 1
    triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    expected1 = 11
    result1 = solver.minimumTotal(triangle1)
    print("Input:", triangle1)
    print("Output:", result1, " Expected:", expected1)
    print("PASS" if result1 == expected1 else "FAIL")
    print("-" * 20)

    # Additional sanity checks
    tests = [
        ([[-10]], -10),
        ([[1],[2,3]], 3),
        ([[1],[2,3],[4,5,6]], 7),  # 1 -> 2 -> 4
        ([[1],[2,3],[1,1,1]], 3),  # 1 -> 1 -> 1
    ]

    for tri, expected in tests:
        got = solver.minimumTotal([row[:] for row in tri])
        print("Input:", tri)
        print("Output:", got, " Expected:", expected)
        print("PASS" if got == expected else "FAIL")
        print("-" * 20)