from typing import List

class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        max_l = max(r for l, r in ranges)
        if max_l < right:
            return False
        diff = [0] * (max_l + 2)
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -=1

        a = [0] * (max_l + 2)
        for i in range(1, len(a)):
            a[i] = a[i-1] + diff[i]

        for i in range(left, right + 1):
            if a[i] < 1:
                return False

        return True

ranges = [[1, 10], [10, 20]]
left = 21
right = 21
s = Solution()
print(s.isCovered(ranges,left,right))