from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        for i, x in enumerate(batteryPercentages):
            if x > count:
                count += 1

        return count

batteryPercentages = [1, 1, 2, 1, 3]
s = Solution()
print(s.countTestedDevices(batteryPercentages))