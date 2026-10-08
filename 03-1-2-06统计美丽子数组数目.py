from typing import List
from collections import defaultdict
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        s = [0] * (len(nums) + 1)
        for i,x in enumerate(nums):
            s[i+1] = s[i] ^ x

        idx = defaultdict(int)
        cnt = 0
        for sj in s:
            cnt += idx[sj]
            idx[sj] += 1

        return cnt

nums = [4,3,1,2,4]
s = Solution()
print(s.beautifulSubarrays(nums))