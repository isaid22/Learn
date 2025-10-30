## Learning how to solve problems

### Array Problems

#### Minimum Product Sum of Two Arrays

**Problem**: Given two arrays `nums1` and `nums2` of equal length, find the minimum product sum by rearranging elements in `nums1`. The product sum is the sum of `a[i] * b[i]` for all indices.

**Solution**: Sort `nums1` in ascending order and `nums2` in descending order, then pair them up. This ensures we multiply the smallest elements with the largest elements, minimizing the total sum.

**Files**: `minimum_product_sum.py`

**Time Complexity**: O(n log n)  
**Space Complexity**: O(1)
