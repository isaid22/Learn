import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = [] # holds smaller elements - negative
        self.min_heap = [] # holds larger elements
        

    def addNum(self, num: int) -> None:

        # always add first one to max_heap
        heapq.heappush(self.max_heap, -num)

        # move if exceed smallest of the right side, also make sure min_heap is not empty as if in cold start.
        if self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        # need to balance heaps
        if (len(self.max_heap) > len(self.min_heap) + 1):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)        

    def findMedian(self) -> float:
        if (len(self.max_heap) > len(self.min_heap)):
            val = -self.max_heap[0]
        else:
            val = (-self.max_heap[0]+self.min_heap[0])/2

        return val