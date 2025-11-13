import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Calculates the minimum cost to connect all points using Prim's algorithm.
        This problem is equivalent to finding the Minimum Spanning Tree (MST) of a graph
        where points are vertices and the edge weight is the Manhattan distance.
        
        Time Complexity: O(N^2 * log N), where N is the number of points.
                         This is because in the worst case, we might add O(N) edges for each of the N vertices.
                         A more optimized Prim's can achieve O(N^2), but this is clear and passes.
        Space Complexity: O(N^2) in the worst case for the heap.
        """
        N = len(points)
        if N <= 1:
            return 0

        # A min-heap to store potential edges to add to the MST.
        # Each item is a tuple: (cost, destination_point_index)
        # We start with point 0, with a cost of 0 to connect to the "tree".
        min_heap = [(0, 0)]
        
        # A set to keep track of points already included in the MST.
        visited = set()
        
        total_cost = 0
        
        # We need to connect N points, so the MST will have N-1 edges.
        # The loop continues as long as we have points to visit and edges to consider.
        while len(visited) < N:
            # 1. Get the cheapest edge from the heap that connects to an unvisited point.
            cost, i = heapq.heappop(min_heap)
            
            # 2. If this point is already in our MST, skip it to avoid cycles.
            if i in visited:
                continue
            
            # 3. Add the point to our MST and add the edge's cost.
            visited.add(i)
            total_cost += cost
            
            # 4. Add new potential edges from this new point to all unvisited neighbors.
            for j in range(N):
                if j not in visited:
                    # Calculate Manhattan distance
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (dist, j))
                    
        return total_cost

if __name__ == '__main__':
    # Example Usage
    solution = Solution()
    
    # Test Case 1
    points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(f"Input: {points1}")
    result1 = solution.minCostConnectPoints(points1)
    print(f"Output: {result1}") # Expected: 20
    print("-" * 20)

    # Test Case 2
    points2 = [[3,12],[-2,5],[-4,1]]
    print(f"Input: {points2}")
    result2 = solution.minCostConnectPoints(points2)
    print(f"Output: {result2}") # Expected: 18
    print("-" * 20)
