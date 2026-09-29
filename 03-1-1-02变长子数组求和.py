from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + nums[i]

        self.s = s
        ans = 0
        for i in range(len(nums)):
            ans += s[i + 1] - s[max(0, i-nums[i])]

        return ans