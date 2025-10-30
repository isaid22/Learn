"""
Runtime optimization techniques for the minimum product sum problem
"""
from typing import List
import time
import random

class Solution:
    def minProductSum_original(self, nums1: List[int], nums2: List[int]) -> int:
        """Your current solution - baseline"""
        nums1_sorted_ascend = sorted(nums1)  # asc order
        
        # get index sorted by descending-ordered value
        nums2_idx_sorted_descval = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        running_sum = 0
        
        # now element-wise multiply
        for i in range(len(nums2)):
            running_sum += nums2[nums2_idx_sorted_descval[i]] * nums1_sorted_ascend[i]
        
        return running_sum

    def minProductSum_optimized1(self, nums1: List[int], nums2: List[int]) -> int:
        """Optimization 1: Avoid index lookup in loop"""
        nums1_sorted = sorted(nums1)
        nums2_sorted_desc = sorted(nums2, reverse=True)
        
        return sum(a * b for a, b in zip(nums1_sorted, nums2_sorted_desc))

    def minProductSum_optimized2(self, nums1: List[int], nums2: List[int]) -> int:
        """Optimization 2: In-place sorting (modifies input)"""
        nums1.sort()  # In-place sorting (faster than creating new list)
        nums2.sort(reverse=True)
        
        total = 0
        for i in range(len(nums1)):
            total += nums1[i] * nums2[i]
        
        return total

    def minProductSum_optimized3(self, nums1: List[int], nums2: List[int]) -> int:
        """Optimization 3: Use built-in sum with generator (most Pythonic)"""
        nums1.sort()
        nums2.sort(reverse=True)
        
        return sum(a * b for a, b in zip(nums1, nums2))

    def minProductSum_no_extra_sort(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Optimization 4: Your approach but with list comprehension to avoid index lookup
        (If you must keep nums2 order intact)
        """
        nums1_sorted = sorted(nums1)
        nums2_indices_by_value = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        
        # Create the reordered nums2 values in one go
        nums2_reordered = [nums2[i] for i in nums2_indices_by_value]
        
        return sum(a * b for a, b in zip(nums1_sorted, nums2_reordered))

    def minProductSum_fastest(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Optimization 5: Fastest approach - sort both arrays directly
        This is the most efficient if you don't need to preserve original arrays
        """
        return sum(a * b for a, b in zip(sorted(nums1), sorted(nums2, reverse=True)))


def benchmark_solutions():
    """Benchmark different solutions"""
    solution = Solution()
    
    # Create test data
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        print(f"\n{'='*50}")
        print(f"Benchmarking with array size: {size}")
        print(f"{'='*50}")
        
        # Generate random test data
        nums1 = [random.randint(1, 100) for _ in range(size)]
        nums2 = [random.randint(1, 100) for _ in range(size)]
        
        methods = [
            ("Original (your approach)", solution.minProductSum_original),
            ("Optimized 1: Direct sort", solution.minProductSum_optimized1),
            ("Optimized 3: Most Pythonic", solution.minProductSum_optimized3),
            ("Optimized 4: List comprehension", solution.minProductSum_no_extra_sort),
            ("Optimized 5: Fastest", solution.minProductSum_fastest),
        ]
        
        results = {}
        
        for name, method in methods:
            # Make copies to ensure fair comparison
            nums1_copy = nums1.copy()
            nums2_copy = nums2.copy()
            
            # Time the method
            start_time = time.perf_counter()
            result = method(nums1_copy, nums2_copy)
            end_time = time.perf_counter()
            
            runtime = (end_time - start_time) * 1000  # Convert to milliseconds
            results[name] = (runtime, result)
            
            print(f"{name:30s}: {runtime:8.4f} ms")
        
        # Verify all results are the same
        result_values = [result[1] for result in results.values()]
        if len(set(result_values)) == 1:
            print(f"{'All results match':30s}: ✓ ({result_values[0]})")
        else:
            print(f"{'ERROR - Results differ':30s}: ✗")


def show_optimization_techniques():
    """Show specific optimization techniques"""
    print("OPTIMIZATION TECHNIQUES:")
    print("="*50)
    
    print("\n1. AVOID INDEX LOOKUPS IN LOOPS")
    print("   Bad:  for i in range(n): sum += arr[indices[i]] * other[i]")
    print("   Good: reorder = [arr[i] for i in indices]; sum(a*b for a,b in zip(...))")
    
    print("\n2. USE BUILT-IN FUNCTIONS")
    print("   Bad:  manual loop with running_sum += ...")
    print("   Good: sum(generator_expression)")
    
    print("\n3. MINIMIZE MEMORY ALLOCATIONS")
    print("   Bad:  nums_sorted = sorted(nums)  # Creates new list")
    print("   Good: nums.sort()                # In-place sorting")
    
    print("\n4. USE GENERATOR EXPRESSIONS")
    print("   Bad:  [a*b for a,b in zip(...)]  # Creates list then sum")
    print("   Good: sum(a*b for a,b in zip(...))  # No intermediate list")
    
    print("\n5. SIMPLIFY THE ALGORITHM")
    print("   Your approach: Sort indices by values, then lookup")
    print("   Better approach: Just sort both arrays directly")


if __name__ == "__main__":
    show_optimization_techniques()
    benchmark_solutions()