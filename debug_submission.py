"""
Debugging the LeetCode submission
"""
from typing import List

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sorted_ascend = sorted(nums1)  # asc order

        # get index sorted by descending-ordered value
        nums2_idx_sorted_descval = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        running_sum = 0
        
        # FIXED: Correct the multiplication logic
        for i in range(len(nums2)):
            # We want to pair:
            # - smallest nums1 element (nums1_sorted_ascend[i])
            # - with position where nums2 has largest value (nums2_idx_sorted_descval[i])
            nums2_index = nums2_idx_sorted_descval[i]
            running_sum += nums1_sorted_ascend[i] * nums2[nums2_index]
        
        # FIXED: Add return statement
        return running_sum


# Let's trace through your original logic vs corrected logic
def debug_original_vs_fixed():
    nums1 = [5, 3, 4, 2]
    nums2 = [4, 2, 2, 5]
    
    print("Input:")
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print()
    
    nums1_sorted_ascend = sorted(nums1)
    nums2_idx_sorted_descval = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
    
    print("After sorting:")
    print(f"nums1_sorted_ascend = {nums1_sorted_ascend}")
    print(f"nums2_idx_sorted_descval = {nums2_idx_sorted_descval}")
    print()
    
    print("What nums2_idx_sorted_descval means:")
    for i, idx in enumerate(nums2_idx_sorted_descval):
        print(f"  Position {i}: index {idx} → nums2[{idx}] = {nums2[idx]}")
    print()
    
    # Original (incorrect) logic
    print("YOUR ORIGINAL LOGIC (INCORRECT):")
    running_sum_original = 0
    for i in range(len(nums2)):
        # This is what you had: nums2[nums2_idx_sorted_descval[i]] * nums1[i]
        value = nums2[nums2_idx_sorted_descval[i]] * nums1[i]  # WRONG: using original nums1
        running_sum_original += value
        print(f"  i={i}: nums2[{nums2_idx_sorted_descval[i]}] * nums1[{i}] = {nums2[nums2_idx_sorted_descval[i]]} * {nums1[i]} = {value}")
    print(f"Original logic sum: {running_sum_original}")
    print()
    
    # Corrected logic
    print("CORRECTED LOGIC:")
    running_sum_fixed = 0
    for i in range(len(nums2)):
        nums2_index = nums2_idx_sorted_descval[i]
        value = nums1_sorted_ascend[i] * nums2[nums2_index]  # CORRECT: using sorted nums1
        running_sum_fixed += value
        print(f"  i={i}: nums1_sorted[{i}] * nums2[{nums2_index}] = {nums1_sorted_ascend[i]} * {nums2[nums2_index]} = {value}")
    print(f"Fixed logic sum: {running_sum_fixed}")
    print()
    
    # Test with Solution class
    solution = Solution()
    result = solution.minProductSum(nums1.copy(), nums2.copy())
    print(f"Solution class result: {result}")
    print(f"Expected result: 40")


if __name__ == "__main__":
    debug_original_vs_fixed()