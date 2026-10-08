from typing import List

# 动态规划方法，没有用前缀和

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        f = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > f[i-1] + nums[i]:
                f[i] = nums[i]
            else:
                f[i] = f[i-1] + nums[i]

        return max(f)

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))