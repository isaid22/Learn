from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []   # edge case: empty tree

        res = []                # final result
        q = deque([root])       # queue starts with the root node

        while q:
            level_size = len(q) # number of nodes at this level
            level = []          # collect values for this level

            for _ in range(level_size):
                node = q.popleft()   # pop from front (FIFO)
                level.append(node.val)

                # add child nodes for the next level
                if node.left:
                    q.append(node.left) # will be processed in next q level
                if node.right:
                    q.append(node.right)# will be processed in next q level
                # now go back to next node in the current level in for loop

            res.append(level)   # completed this level, add to result.

        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1: root = [3,9,20,null,null,15,7]
    # Tree:
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    print("Example 1:")
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    result1 = sol.levelOrder(root1)
    print(f"Input: [3,9,20,null,null,15,7]")
    print(f"Output: {result1}")
    print(f"Expected: [[3],[9,20],[15,7]]")
    print(f"Correct: {result1 == [[3],[9,20],[15,7]]} ✓\n")


    # Example 2: root = [1]
    print("Example 2:")
    root2 = TreeNode(1)
    result2 = sol.levelOrder(root2)
    print(f"Input: [1]")
    print(f"Output: {result2}")
    print(f"Expected: [[1]]")
    print(f"Correct: {result2 == [[1]]} ✓\n")

    # Example 3: root = []
    print("Example 3:")
    root3 = None
    result3 = sol.levelOrder(root3)
    print(f"Input: []")
    print(f"Output: {result3}")
    print(f"Expected: []")
    print(f"Correct: {result3 == []} ✓\n")

    print("All tests completed! 🎉")
