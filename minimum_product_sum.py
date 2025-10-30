"""
Minimum Product Sum of Two Arrays

The product sum of two equal-length arrays a and b is equal to the sum of a[i] * b[i] 
for all 0 <= i < a.length (0-indexed).

Given two arrays nums1 and nums2 of length n, return the minimum product sum 
if you are allowed to rearrange the order of the elements in nums1.

Strategy:
To minimize the product sum, we should place the smallest elements from nums1 
at positions where nums2 has the largest values. Since we can only rearrange nums1 
(nums2 order is fixed), we need to strategically position nums1 elements to pair 
small numbers with large numbers, minimizing the overall sum.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) if we don't count the space used by sorting algorithm
"""

from typing import List

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Find the minimum product sum by rearranging nums1.
        
        Args:
            nums1: List of integers that can be rearranged
            nums2: List of integers with FIXED order (cannot be rearranged)
        
        Returns:
            int: The minimum possible product sum
        """
        # Sort nums1 in ascending order (smallest first)
        # We need to pair smallest nums1 elements with largest nums2 elements
        nums1_sorted = sorted(nums1)
        
        # Sort nums2 by value but keep track of original indices to pair correctly
        # We need to find which elements in nums2 are largest to pair with smallest nums1
        nums2_with_indices = [(nums2[i], i) for i in range(len(nums2))]
        nums2_with_indices.sort(key=lambda x: x[0], reverse=True)  # Sort by value, largest first
        
        # Create the optimal arrangement of nums1
        optimal_nums1 = [0] * len(nums1)
        
        # Assign smallest nums1 elements to positions where nums2 has largest elements
        for i in range(len(nums1)):
            nums2_value, nums2_index = nums2_with_indices[i]
            optimal_nums1[nums2_index] = nums1_sorted[i]
        
        # Calculate the product sum
        product_sum = 0
        for i in range(len(nums1)):
            product_sum += optimal_nums1[i] * nums2[i]
        
        return product_sum
    
    def minProductSum_oneliner(self, nums1: List[int], nums2: List[int]) -> int:
        """
        More concise version - pair smallest nums1 with largest nums2 values.
        """
        # Sort nums1 ascending, get nums2 indices sorted by values descending
        nums1_sorted = sorted(nums1)
        nums2_indices_by_value = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        
        # Create optimal nums1 arrangement
        result_nums1 = [0] * len(nums1)
        for i, idx in enumerate(nums2_indices_by_value):
            result_nums1[idx] = nums1_sorted[i]
            
        return sum(result_nums1[i] * nums2[i] for i in range(len(nums1)))


# Helper functions for testing (keeping the original functions for backward compatibility)
def min_product_sum(nums1, nums2):
    """Legacy function - use Solution.minProductSum instead"""
    solution = Solution()
    return solution.minProductSum(nums1.copy(), nums2.copy())


def min_product_sum_one_liner(nums1, nums2):
    """Legacy function - use Solution.minProductSum_oneliner instead"""
    solution = Solution()
    return solution.minProductSum_oneliner(nums1.copy(), nums2.copy())


# Test cases
def test_solution():
    """Test the solution with provided examples"""
    solution = Solution()
    
    # Example 1
    nums1 = [5, 3, 4, 2]
    nums2 = [4, 2, 2, 5]
    result = solution.minProductSum(nums1.copy(), nums2.copy())
    expected = 40
    print(f"Example 1:")
    print(f"nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Test passed: {result == expected}")
    print()
    
    # Example 2
    nums1 = [2, 1, 4, 5, 7]
    nums2 = [3, 2, 4, 8, 6]
    result = solution.minProductSum(nums1.copy(), nums2.copy())
    expected = 65
    print(f"Example 2:")
    print(f"nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Test passed: {result == expected}")
    print()
    
    # Additional test case
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 1]
    result = solution.minProductSum(nums1.copy(), nums2.copy())
    expected = 10  # [1,2,3] with [3,2,1] -> 1*3 + 2*2 + 3*1 = 10
    print(f"Additional test:")
    print(f"nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Test passed: {result == expected}")


def demonstrate_solution():
    """Demonstrate how the algorithm works step by step"""
    solution = Solution()
    nums1 = [5, 3, 4, 2]
    nums2 = [4, 2, 2, 5]
    
    print("Step-by-step demonstration:")
    print(f"Original nums1: {nums1} (can be rearranged)")
    print(f"Original nums2: {nums2} (FIXED - cannot be rearranged)")
    print()
    
    # Show the algorithm
    nums1_sorted = sorted(nums1)
    print(f"nums1 sorted ascending: {nums1_sorted}")
    
    # Find nums2 elements in descending order with their positions
    nums2_with_pos = [(nums2[i], i) for i in range(len(nums2))]
    nums2_with_pos.sort(key=lambda x: x[0], reverse=True)
    
    print("nums2 values with positions (largest first):")
    for value, pos in nums2_with_pos:
        print(f"  Value {value} at position {pos}")
    print()
    
    # Show optimal pairing
    print("Optimal strategy: Place smallest nums1 elements where nums2 has largest values")
    optimal_nums1 = [0] * len(nums1)
    
    for i, (nums2_val, nums2_pos) in enumerate(nums2_with_pos):
        optimal_nums1[nums2_pos] = nums1_sorted[i]
        print(f"Put {nums1_sorted[i]} (smallest remaining from nums1) at position {nums2_pos} to multiply with {nums2_val}")
    
    print(f"\nOptimal nums1 arrangement: {optimal_nums1}")
    print(f"Fixed nums2:               {nums2}")
    print()
    
    # Calculate final result
    print("Final calculation:")
    total = 0
    for i in range(len(nums1)):
        product = optimal_nums1[i] * nums2[i]
        total += product
        print(f"{optimal_nums1[i]} * {nums2[i]} = {product}")
    
    print(f"\nTotal minimum product sum: {total}")
    
    # Verify with our Solution class
    result = solution.minProductSum(nums1.copy(), nums2.copy())
    print(f"Solution.minProductSum result: {result}")
    print(f"Matches manual calculation: {total == result}")


if __name__ == "__main__":
    print("Minimum Product Sum of Two Arrays")
    print("=" * 40)
    print()
    
    # Run tests
    test_solution()
    print()
    
    # Demonstrate the algorithm
    demonstrate_solution()
    
    print("\n" + "=" * 40)
    print("Algorithm explanation:")
    print("1. Sort nums1 in ascending order (smallest first)")
    print("2. Find positions in nums2 with largest values")  
    print("3. Place smallest nums1 elements at those positions")
    print("4. This minimizes the product sum while keeping nums2 order fixed")