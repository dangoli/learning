from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        a = [0] * (len(nums) - 1)
        for i in range(len(nums) - 1):
            a[i] = nums[i]%2 == nums[i+ 1] %2
        s = [0] * len(nums)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + a[i]    
        return [s[from_] == s[to] for from_, to in queries]

nums = [3,4,1,2,6]

queries = [[0,4]]
print(Solution().isArraySpecial(nums, queries))