from typing import List
from collections import defaultdict

# 把0换成-1！！
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = [0] * (len(nums) + 1)
        
        for i,x in enumerate(nums):
            if x == 0:
                x = -1
            s[i+1] = s[i] + x

        # 用字典记录前缀和上一次出现的位置
        diction = {0:0}
        max_l = 0
        for j in range(1, len(s)):
            
            if s[j] not in diction:
                diction[s[j]] = j
            else:
                max_l = max(max_l, j - diction[s[j]])
            

        return max_l

nums = [0,1,1,1,1,1,0,0,0]
s = Solution()
print(s.findMaxLength(nums))