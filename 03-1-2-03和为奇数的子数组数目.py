from typing import List
from collections import defaultdict
MOD = 10**9 + 7

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        s = [0] * (len(arr) + 1)
        for i,x in enumerate(arr):
            s[i+1] = s[i] + x
        cnt = 0

        idx_jo = {"even": 1, "odd": 0}
        for j in range(1, len(s)):
            cnt += (idx_jo["odd"] if s[j] % 2 == 0 else idx_jo["even"])
            if s[j] % 2 == 0:
                idx_jo["even"] += 1
            else:
                idx_jo["odd"] += 1

        cnt = cnt % MOD
        return cnt

nums = [1,3,5]
s = Solution()
print(s.numOfSubarrays(nums))