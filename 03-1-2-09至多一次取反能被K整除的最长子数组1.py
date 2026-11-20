from typing import List

class Solution:
    def longestSubarrayDivK(self, nums: list[int], k: int) -> int:
        p = [0] # 前缀和取余
        total = 0
        for i, x in enumerate(nums):
            total += x
            p.append(total % k)

        first_p = {0 : 0} # 记录取余后首次出现的下标
        ans_l = 0
        for i,x in enumerate(p):
            if x in first_p:
                ans_l = max(ans_l, i - first_p[x])
            else:
                first_p[x] = i
        return ans_l

    def longestSubarray(self, nums: list[int], k: int) -> int:
        # 枚举取反的numsi
        ans_l = self.longestSubarrayDivK(nums, k) # 先算不取反的情况
        for i in range(len(nums)):
            nums[i] *= -1
            ans_l = max(ans_l, self.longestSubarrayDivK(nums, k))
            nums[i] *= -1 #复原

        return ans_l

nums = [4,1,2]
k = 3
s = Solution()
print(s.longestSubarray(nums, k))