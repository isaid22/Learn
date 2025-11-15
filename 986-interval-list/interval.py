from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]

            # Compute overlap
            start = max(a1, b1)
            end = min(a2, b2)
            if start <= end:                # closed intervals: touching counts
                res.append([start, end])

            # Move the pointer that ends first
            if a2 < b2:
                i += 1
            else:
                j += 1

        return res

if __name__ == "__main__":
    sol = Solution()

    # Helper to print results
    def run_test(test_name, firstList, secondList, expected):
        print(f"--- {test_name} ---")
        print(f"firstList:  {firstList}")
        print(f"secondList: {secondList}")
        result = sol.intervalIntersection(firstList, secondList)
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Correct:  {result == expected} ✓\n")

    # Example 1
    firstList1 = [[0,2],[5,10],[13,23],[24,25]]
    secondList1 = [[1,5],[8,12],[15,24],[25,26]]
    expected1 = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    run_test("Example 1", firstList1, secondList1, expected1)

    # Example 2
    firstList2 = [[1,3],[5,9]]
    secondList2 = []
    expected2 = []
    run_test("Example 2", firstList2, secondList2, expected2)

    # Additional test case: No intersection
    firstList3 = [[1,2],[3,4]]
    secondList3 = [[5,6],[7,8]]
    expected3 = []
    run_test("No Intersection", firstList3, secondList3, expected3)
    
    print("All tests completed! 🎉")