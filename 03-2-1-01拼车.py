from typing import List
from collections import defaultdict

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        d = defaultdict(int)
        for num, from_, to_ in trips:
            d[from_] += num
            d[to_] -= num

        s = 0
        for x in sorted(d):
            s += d[x]
            if s > capacity:
                return False

        return True

trips = [[2,1,5],[3,3,7]]
capacity = 5
s = Solution()
print(s.carPooling(trips, capacity))