from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        s = [0] * (len(nums) + 1)
        for i,x in enumerate(nums):
            s[i+1] = s[i] + x

        cnt = 0
        cnt_i = defaultdict(int)
        for sj in s:
            cnt += cnt_i[sj-goal]
            cnt_i[sj] += 1

        return cnt

nums = [0,0,0,0,0]
goal = 0
s = Solution()
print(s.numSubarraysWithSum(nums, goal))