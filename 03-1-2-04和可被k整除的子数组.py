from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        l = [0]
        total = 0
        for x in nums:
            total += x
            l.append(total % k)

        cnt = 0
        idx = defaultdict(int)
        for sj in l:
            cnt += idx[sj]
            idx[sj] += 1

        return cnt

nums = [4,5,0,-2,-3,1]
s = Solution()
k = 5
print(s.subarraysDivByK(nums, k))