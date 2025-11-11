from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                # if this is the last node in the level, add it
                if i == level_size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [1,2,3,null,5,null,4]
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    print("Example 1: [1,2,3,null,5,null,4]")
    print("Tree structure:")
    print("      1")
    print("     / \\")
    print("    2   3")
    print("     \\   \\")
    print("      5   4")
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    
    result1 = sol.rightSideView(root1)
    print(f"Output: {result1}")
    print(f"Expected: [1, 3, 4]")
    print(f"Correct: {result1 == [1, 3, 4]} ✓\n")
    
    # Example 2: [1,2,3,4,null,null,null,5]
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    #  /
    # 5
    print("Example 2: [1,2,3,4,null,null,null,5]")
    print("Tree structure:")
    print("      1")
    print("     / \\")
    print("    2   3")
    print("   /")
    print("  4")
    print(" /")
    print("5")
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.left.left = TreeNode(5)
    
    result2 = sol.rightSideView(root2)
    print(f"Output: {result2}")
    print(f"Expected: [1, 3, 4, 5]")
    print(f"Correct: {result2 == [1, 3, 4, 5]} ✓\n")
    
    # Example 3: Empty tree
    print("Example 3: Empty tree")
    root3 = None
    result3 = sol.rightSideView(root3)
    print(f"Output: {result3}")
    print(f"Expected: []")
    print(f"Correct: {result3 == []} ✓\n")
    
    # Example 4: Single node
    print("Example 4: Single node [1]")
    root4 = TreeNode(1)
    result4 = sol.rightSideView(root4)
    print(f"Output: {result4}")
    print(f"Expected: [1]")
    print(f"Correct: {result4 == [1]} ✓\n")
    
    # Example 5: Only left children
    # Tree:  1
    #       /
    #      2
    #     /
    #    3
    print("Example 5: Only left children")
    print("Tree structure:")
    print("  1")
    print(" /")
    print("2")
    print("/")
    print("3")
    
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    
    result5 = sol.rightSideView(root5)
    print(f"Output: {result5}")
    print(f"Expected: [1, 2, 3]")
    print(f"Correct: {result5 == [1, 2, 3]} ✓\n")
    
    print("All tests completed! 🎉")