from typing import List

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Find the minimum product sum by rearranging nums1 only.
        nums2 order is FIXED and cannot be changed.
        
        Strategy: Place smallest nums1 elements at positions where 
        nums2 has the largest values.
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(n) for the result array
        """
        # Sort nums1 in ascending order
        nums1_sorted = sorted(nums1)
        
        # Get indices of nums2 sorted by their values (largest first)
        nums2_indices_by_value = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        
        # Create optimal arrangement of nums1
        result_nums1 = [0] * len(nums1)
        for i, idx in enumerate(nums2_indices_by_value):
            result_nums1[idx] = nums1_sorted[i]
        
        # Calculate product sum
        return sum(result_nums1[i] * nums2[i] for i in range(len(nums1)))

# Alternative implementation:
class SolutionAlternative:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Alternative approach using value-index pairs.
        """
        nums1_sorted = sorted(nums1)
        nums2_with_indices = sorted([(nums2[i], i) for i in range(len(nums2))], 
                                  key=lambda x: x[0], reverse=True)
        
        optimal_nums1 = [0] * len(nums1)
        for i, (_, nums2_index) in enumerate(nums2_with_indices):
            optimal_nums1[nums2_index] = nums1_sorted[i]
        
        return sum(optimal_nums1[i] * nums2[i] for i in range(len(nums1)))
        