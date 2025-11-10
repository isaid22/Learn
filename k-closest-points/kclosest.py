import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin using a max-heap of size k.
        
        Time Complexity: O(N log k)
        Space Complexity: O(k)
        """
        # The heap will store tuples of (-distance, x, y)
        # We use negative distance to simulate a max-heap with Python's min-heap
        max_heap = []
        
        for (x, y) in points:
            # Calculate the squared Euclidean distance
            dist = -(x*x + y*y)
            
            # If the heap is not yet full, just add the point
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            # If the new point is closer than the farthest point in the heap
            elif dist > max_heap[0][0]:
                # Replace the farthest point with the new, closer point
                heapq.heappushpop(max_heap, (dist, x, y))
        
        # The heap now contains the k closest points.
        # The first element of each tuple is the negative distance, which we don't need.
        # We just need to return the points (x, y).
        return [[x, y] for (dist, x, y) in max_heap]

if __name__ == '__main__':
    # Example Usage
    solution = Solution()
    
    # Test Case 1
    points1 = [[1, 3], [-2, 2]]
    k1 = 1
    result1 = solution.kClosest(points1, k1)
    print(f"Input: points = {points1}, k = {k1}")
    print(f"Output: {result1}") # Expected: [[-2, 2]]
    print("-" * 20)

    # Test Case 2
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    result2 = solution.kClosest(points2, k2)
    print(f"Input: points = {points2}, k = {k2}")
    print(f"Output: {result2}") # Expected: [[3, 3], [-2, 4]] (order may vary)
    print("-" * 20)
