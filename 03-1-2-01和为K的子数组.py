from typing import List
from collections import defaultdict
# 计算数组前缀和
# 枚举右边的j,检查左边有没有i满足s[j] - k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums)+1)
        for i,x in enumerate(nums):
            s[i+1] = s[i] + x
        cnt = 0

        idx = defaultdict(int)
        for sj in s:
            cnt += idx[sj - k]
            idx[sj] += 1

        return cnt

nums = [1]
k = 1  
s = Solution()
print(s.subarraySum(nums, k))