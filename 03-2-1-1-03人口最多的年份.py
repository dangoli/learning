from typing import List

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        diff = [0] * 2052
        for birth, death in logs:
            diff[birth] += 1
            diff[death] -= 1

        s = 0
        max_s = 0
        ans = 0

        for i,x in enumerate(diff):
            s += x
            if max_s < s:
                max_s = s
                ans = i

        return ans

logs = [[1993, 1999], [2000, 2010]]
s = Solution()
print(s.maximumPopulation(logs))