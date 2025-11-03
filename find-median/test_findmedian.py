# Testing the findmedian_submit.py implementation

import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # holds smaller elements - negative
        self.min_heap = []  # holds larger elements
        
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

def test_different_orders():
    print("🧪 TESTING YOUR IMPLEMENTATION WITH DIFFERENT INPUT ORDERS")
    print("=" * 70)
    
    # Test 1: Sorted order
    print("Test 1: Adding numbers in sorted order [1, 2, 3, 4, 5]")
    mf1 = MedianFinder()
    for num in [1, 2, 3, 4, 5]:
        mf1.addNum(num)
        median = mf1.findMedian()
        max_vals = [-x for x in mf1.max_heap]
        print(f"  Added {num}: max_heap={max_vals}, min_heap={mf1.min_heap}, median={median}")
    
    print()
    
    # Test 2: Reverse sorted order
    print("Test 2: Adding numbers in reverse order [5, 4, 3, 2, 1]")
    mf2 = MedianFinder()
    for num in [5, 4, 3, 2, 1]:
        mf2.addNum(num)
        median = mf2.findMedian()
        max_vals = [-x for x in mf2.max_heap]
        print(f"  Added {num}: max_heap={max_vals}, min_heap={mf2.min_heap}, median={median}")
    
    print()
    
    # Test 3: Random order
    print("Test 3: Adding numbers in random order [3, 1, 5, 2, 4]")
    mf3 = MedianFinder()
    for num in [3, 1, 5, 2, 4]:
        mf3.addNum(num)
        median = mf3.findMedian()
        max_vals = [-x for x in mf3.max_heap]
        print(f"  Added {num}: max_heap={max_vals}, min_heap={mf3.min_heap}, median={median}")
    
    print()
    
    # Check if all final medians are the same
    final_median1 = mf1.findMedian()
    final_median2 = mf2.findMedian()
    final_median3 = mf3.findMedian()
    
    print(f"Final medians:")
    print(f"  Sorted order: {final_median1}")
    print(f"  Reverse order: {final_median2}")
    print(f"  Random order: {final_median3}")
    print(f"  All same? {final_median1 == final_median2 == final_median3}")
    
    return final_median1 == final_median2 == final_median3

def test_edge_cases():
    print("\n🧪 TESTING EDGE CASES")
    print("=" * 40)
    
    # Single element
    print("Test: Single element")
    mf = MedianFinder()
    mf.addNum(42)
    print(f"  Median of [42]: {mf.findMedian()}")
    
    # Two elements
    print("Test: Two elements")
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(f"  Median of [1,2]: {mf.findMedian()}")
    
    # Duplicates
    print("Test: Duplicate elements")
    mf = MedianFinder()
    for num in [5, 5, 5, 5]:
        mf.addNum(num)
    print(f"  Median of [5,5,5,5]: {mf.findMedian()}")
    
    # Negative numbers
    print("Test: Negative numbers")
    mf = MedianFinder()
    for num in [-1, -2, 0, 1, 2]:
        mf.addNum(num)
    print(f"  Median of [-1,-2,0,1,2]: {mf.findMedian()}")

if __name__ == "__main__":
    order_independent = test_different_orders()
    test_edge_cases()
    
    print(f"\n✅ CONCLUSION: Your implementation {'WORKS' if order_independent else 'FAILS'} regardless of input order!")