from typing import List
from itertools import accumulate

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        max_end = max(end for _, end in nums)
        diff = [0] * (max_end + 2)
        for start, end in nums:
            diff[start] += 1
            diff[end + 1] -= 1

        sd = accumulate(diff) # accumulate 
        return sum( s > 0 for s in sd)

nums = [[3, 6], [1, 5], [4, 7]]
s = Solution()
print(s.numberOfPoints(nums))