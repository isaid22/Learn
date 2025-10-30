"""
Solutions for NumPy-style multiplication in LeetCode
"""
from typing import List
import numpy as np

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Method 1: Pure Python with list comprehension (RECOMMENDED for LeetCode)
        """
        nums1_sorted_ascend = sorted(nums1)
        nums2_idx_sorted_descval = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        
        # Extract nums2 values in the order we want using list comprehension
        nums2_ordered = [nums2[i] for i in nums2_idx_sorted_descval]
        
        # Calculate sum of element-wise products
        return sum(a * b for a, b in zip(nums1_sorted_ascend, nums2_ordered))

class SolutionNumPy:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Method 2: Using NumPy (works but not recommended for LeetCode)
        """
        nums1_sorted_ascend = sorted(nums1)
        nums2_idx_sorted_descval = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        
        # Convert to NumPy arrays first, then use fancy indexing
        nums2_np = np.array(nums2)
        nums2_ordered = nums2_np[nums2_idx_sorted_descval]
        
        # Element-wise multiplication and sum
        result_array_np = np.array(nums1_sorted_ascend) * nums2_ordered
        return int(np.sum(result_array_np))  # Convert to int for LeetCode

class SolutionManualLoop:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Method 3: Your original approach with manual loop (also works)
        """
        nums1_sorted_ascend = sorted(nums1)
        nums2_idx_sorted_descval = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        
        running_sum = 0
        for i in range(len(nums2)):
            running_sum += nums1_sorted_ascend[i] * nums2[nums2_idx_sorted_descval[i]]
        
        return running_sum

def test_all_methods():
    """Test all three methods"""
    nums1 = [5, 3, 4, 2]
    nums2 = [4, 2, 2, 5]
    
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Expected output: 40")
    print()
    
    # Test Method 1: Pure Python
    solution1 = Solution()
    result1 = solution1.minProductSum(nums1.copy(), nums2.copy())
    print(f"Method 1 (Pure Python): {result1}")
    
    # Test Method 2: NumPy
    solution2 = SolutionNumPy()
    result2 = solution2.minProductSum(nums1.copy(), nums2.copy())
    print(f"Method 2 (NumPy): {result2}")
    
    # Test Method 3: Manual loop
    solution3 = SolutionManualLoop()
    result3 = solution3.minProductSum(nums1.copy(), nums2.copy())
    print(f"Method 3 (Manual loop): {result3}")
    
    print(f"\nAll methods work: {result1 == result2 == result3 == 40}")

def demonstrate_fancy_indexing_issue():
    """Demonstrate the fancy indexing issue"""
    nums2 = [4, 2, 2, 5]
    indices = [3, 0, 1, 2]
    
    print("Demonstrating the fancy indexing issue:")
    print(f"nums2 = {nums2}")
    print(f"indices = {indices}")
    print()
    
    # This fails with Python lists
    print("❌ This FAILS with Python lists:")
    print("nums2[indices]  # TypeError!")
    try:
        result = nums2[indices]
    except TypeError as e:
        print(f"Error: {e}")
    print()
    
    # This works with NumPy arrays
    print("✅ This WORKS with NumPy arrays:")
    nums2_np = np.array(nums2)
    result = nums2_np[indices]
    print(f"np.array(nums2)[indices] = {result}")
    print()
    
    # Python list alternative
    print("✅ Python list alternative:")
    result_list = [nums2[i] for i in indices]
    print(f"[nums2[i] for i in indices] = {result_list}")

if __name__ == "__main__":
    demonstrate_fancy_indexing_issue()
    print("\n" + "="*50 + "\n")
    test_all_methods()