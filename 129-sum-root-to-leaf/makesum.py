# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional['TreeNode']) -> int:
        """
        Calculate the sum of all root-to-leaf numbers.
        
        Approach: DFS traversal where we build numbers as we traverse down
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height (recursion stack)
        """
        def dfs(node, current_number):
            """
            DFS helper function to traverse and calculate sum.
            
            Args:
                node: Current tree node
                current_number: Number formed from root to current node's parent
            
            Returns:
                Sum of all numbers formed from current node to its leaf descendants
            """
            if not node:
                return 0
            
            # Build the current number by appending current node's digit
            current_number = current_number * 10 + node.val
            
            # If it's a leaf node, return the complete number
            if not node.left and not node.right:
                return current_number
            
            # Otherwise, recursively calculate sum from left and right subtrees
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)
            
            return left_sum + right_sum
        
        return dfs(root, 0)


# Alternative iterative solution using stack
class SolutionIterative:
    def sumNumbers(self, root: Optional['TreeNode']) -> int:
        """
        Iterative approach using stack.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return 0
        
        total_sum = 0
        stack = [(root, 0)]  # (node, number_so_far)
        print(stack)
        while stack:
            node, current_number = stack.pop()
            current_number = current_number * 10 + node.val
            
            # If leaf node, add to total sum
            if not node.left and not node.right:
                total_sum += current_number
            
            # Add children to stack
            if node.right:
                stack.append((node.right, current_number))
            if node.left:
                stack.append((node.left, current_number))
        
        return total_sum


# Test cases
if __name__ == "__main__":
    # Helper class for testing
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    # Example 1: [1,2,3]
    # Tree structure:
    #     1
    #    / \
    #   2   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    
    sol = Solution()
    print(f"Example 1: {sol.sumNumbers(root1)}")  # Expected: 25 (12 + 13)
    
    # Example 2: [4,9,0,5,1]
    # Tree structure:
    #       4
    #      / \
    #     9   0
    #    / \
    #   5   1
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    
    print(f"Example 2: {sol.sumNumbers(root2)}")  # Expected: 1026 (495 + 491 + 40)
    
    # Test with iterative solution
    sol_iter = SolutionIterative()
    print(f"\nIterative Solution:")
    print(f"Example 1: {sol_iter.sumNumbers(root1)}")  # Expected: 25
    print(f"Example 2: {sol_iter.sumNumbers(root2)}")  # Expected: 1026
