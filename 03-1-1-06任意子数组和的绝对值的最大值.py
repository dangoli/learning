from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = [0] * (len(nums) + 1)
        max_s = min_s = 0
        for i, x in enumerate(nums):
            s[i+1] = s[i] + x
            if s[i+1] > max_s:
                max_s = s[i+1]
            elif s[i+1] < min_s:
                min_s = s[i+1]

        return abs(max_s - min_s)

nums = [1,-3,2,3,-4]
s1 = Solution()
print(s1.maxAbsoluteSum(nums))