from typing import List

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        xor_n = [0] * (len(nums) + 1) # 异或前缀和
        balance = [0] * (len(nums) + 1) # 奇数量减去偶数量的差
        for i, x in enumerate(nums):
            xor_n[i+1] = xor_n[i] ^ x
            if x % 2:
                balance[i+1] = balance[i] + 1
            else:
                balance[i+1] = balance[i] - 1

        first_p = {(0,0): 0} # 记录异或yiji奇偶差第一次出现下标
        ans = 0
        for i,p in enumerate(xor_n):
            if (p, balance[i]) in first_p:
                ans = max(ans, i - first_p[(p, balance[i])])
            else:
                first_p[(p,balance[i])] = i
        return ans

nums = [3,1,3,2,0]
s = Solution()
print(s.maxBalancedSubarray(nums))