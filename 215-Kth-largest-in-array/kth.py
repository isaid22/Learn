import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


        """
        | Operation     | Complexity   |
| ------------- | ------------ |
| Each push/pop | `O(log k)`   |
| Total         | `O(n log k)` |
| Space         | `O(k)`       |

Example walkthrough        
    nums = [3,2,1,5,6,4], k = 2

Step-by-step:
heap = []
push 3 → [3]
push 2 → [2,3]
push 1 → [1,3,2] → pop smallest (1) → [2,3]
push 5 → [2,3,5] → pop smallest (2) → [3,5]
push 6 → [3,5,6] → pop smallest (3) → [5,6]
push 4 → [4,5,6] → pop smallest (4) → [5,6]

=> min_heap[0] = 5
        
        Every time we push a new number onto the heap, we check if the heap size exceeds k.
        If it does, we pop the smallest element. This way, we maintain a heap of size k
        containing the k largest elements seen so far. The smallest element in this heap 
        (the root of the min-heap) is the k-th largest element in the entire array. We make cleer use of bottom og a heap. 
        """