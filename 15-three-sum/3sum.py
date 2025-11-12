import typing
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n):
            # Stop early: once nums[i] > 0, sum can't be zero
            if nums[i] > 0:
                break

            # Skip duplicate first elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates for the second element
                    l_val = nums[l]
                    while l < r and nums[l] == l_val:
                        l += 1
                    # Skip duplicates for the third element
                    r_val = nums[r]
                    while l < r and nums[r] == r_val:
                        r -= 1

        return res

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]]),
        ([0,0,0,0], [[0,0,0]]),
        ([-2,0,1,1,2], [[-2,0,2], [-2,1,1]]),
        ([], []),
        ([3,-2,-1,0], [[-2,-1,3]]),  # corrected expected: (-2)+(-1)+3=0
        ([-4,-2,-2,-2,0,1,2,2,2,3], [[-4,1,3], [-4,2,2], [-2,0,2]])  # removed invalid [-2,-1,3]
    ]

    def norm(triplets: List[List[int]]) -> List[List[int]]:
        return sorted([sorted(t) for t in triplets])

    for idx, (inp, expected) in enumerate(tests, 1):
        out = sol.threeSum(inp[:])
        print(f"Test {idx}: nums = {inp}")
        print(f"Output:   {out}")
        print(f"Expected: {expected}")
        print(f"Pass: {norm(out) == norm(expected)}\n")