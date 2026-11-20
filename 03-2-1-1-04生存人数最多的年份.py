from typing import List

class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        diff = [0] * 200 # 生于2000的人最多活100年
        for num in birth:
            diff[num - 1900] += 1

        for num in death:
            diff[num - 1899] -= 1

        s = 0
        max_s = 0
        ans = 0
        for i, x in enumerate(diff):
            s += x
            if max_s < s:
                max_s = s
                ans = i

        return ans+1900

birth = [1900, 1901, 1950]
death = [1948, 1951, 2000]
s = Solution()
print(s.maxAliveYear(birth, death))