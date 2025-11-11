from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2                  # pick middle element
            root = TreeNode(nums[mid])            # make it the root
            root.left = build(lo, mid - 1)        # build left subtree
            root.right = build(mid + 1, hi)       # build right subtree
            return root
        
        return build(0, len(nums) - 1)

if __name__ == '__main__':
    import collections

    def tree_to_level_order_list(root: Optional[TreeNode]) -> List:
        """Helper function to convert a tree to a list for printing."""
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                # Use 'null' string to match LeetCode's output format
                result.append('null')
        
        # Trim trailing 'null's for a cleaner output
        while result and result[-1] == 'null':
            result.pop()
            
        return result

    solver = Solution()

    # Test Case 1
    nums1 = [-10, -3, 0, 5, 9]
    print(f"Input: {nums1}")
    root1 = solver.sortedArrayToBST(nums1)
    output1 = tree_to_level_order_list(root1)
    print(f"Output: {output1}")
    print("-" * 20)

    # Test Case 2
    nums2 = [1, 3]
    print(f"Input: {nums2}")
    root2 = solver.sortedArrayToBST(nums2)
    output2 = tree_to_level_order_list(root2)
    print(f"Output: {output2}")
    print("-" * 20)