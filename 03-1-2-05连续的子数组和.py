from typing import List
from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        s = [0]
        total = 0
        for x in nums:
            total += x
            s.append(total % k)

        cnt = 0
        idx = defaultdict(int)

        for j in range(1, len(s)):
            cnt += idx[s[j]]
            idx[s[j-1]] += 1

        return True if cnt >= 1 else False

nums = [23,2,4,6,7]
k = 6
s = Solution()
print(s.checkSubarraySum(nums, k))