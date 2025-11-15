# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict
from typing import List, Optional

class Solution:
    def verticalTraversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []

        # Step 1: BFS to gather (col, row, val) for every node
        nodes = []  # list of tuples (col, row, val)
        q = deque([(root, 0, 0)])  # (node, row, col), root at (0,0)

        while q:
            node, r, c = q.popleft()
            nodes.append((c, r, node.val))
            if node.left:
                q.append((node.left, r + 1, c - 1))
            if node.right:
                q.append((node.right, r + 1, c + 1))

        # Step 2: sort by col, then row, then val (tie-breaker)
        nodes.sort()  # Python tuples sort lexicographically: col, row, val 
        # [(-1, 1, 9), (0, 0, 3), (0, 2, 15), (1, 1, 20), (2, 2, 7)]
        # Step 3: group by col
        ans = []
        cur_col = None
        cur_bucket = []
        for c, r, v in nodes:
            if cur_col is None:
                cur_col, cur_bucket = c, [v] # make value as list
            elif c == cur_col: # if same column, append value
                cur_bucket.append(v) # append value to current bucket which is a list   
            else: # this must be a new column, so append previous bucket then update cur_col and cur_bucket
                ans.append(cur_bucket)
                cur_col, cur_bucket = c, [v]
        if cur_bucket: # after loop ends, append the last bucket
            ans.append(cur_bucket)

        return ans

if __name__ == "__main__":
    sol = Solution()

    # Helper to print results
    def run_test(test_name, root, expected):
        print(f"--- {test_name} ---")
        result = sol.verticalTraversal(root)
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Correct:  {result == expected} ✓\n")

    # Example 1: root = [3,9,20,null,null,15,7]
    # Tree:
    #     3 (0,0)
    #    / \
    #   9  20 (1,1)
    #  (-1,1)/  \
    #    15   7
    #   (0,2) (2,2)
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    run_test("Example 1", root1, [[9], [3, 15], [20], [7]])

    # Example 2: root = [1,2,3,4,5,6,7]
    # Tree:
    #       1 (0,0)
    #      /   \
    #     2     3
    #   (1,-1) (1,1)
    #   / \   / \
    #  4   5 6   7
    # (2,-2)(2,0)(2,0)(2,2)
    # Note: 5 and 6 are at the same position (2,0), so they must be sorted by value.
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    run_test("Example 2 (Same Position Sort)", root2, [[4], [2], [1, 5, 6], [3], [7]])

    # Example 3: root = []
    run_test("Empty Tree", None, [])

    # Example 4: root = [1]
    root4 = TreeNode(1)
    run_test("Single Node", root4, [[1]])

    print("All tests completed! 🎉")
