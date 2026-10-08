from typing import List

class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        s = [0] * (len(array) + 1)
        array1 = [0] * len(array)
        for i, x in enumerate(array):
            array1[i] = x
            if x >= "A" and x <= "z":
                array[i] = -1
            else:
                array[i] = 1
            s[i+1] = s[i] + array[i]

        # 用字典记录前缀和最初出现的位置
        diction = {0:0}
        max_l = 0
        min_i = 0
        for j in range(1, len(s)):
            if s[j] not in diction:
                diction[s[j]] = j
            else:
                if j - diction[s[j]] > max_l:
                    max_l = j - diction[s[j]]
                    min_i = diction[s[j]]

        return array1[min_i : min_i + max_l]

array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
s = Solution()
print(s.findLongestSubarray(array))