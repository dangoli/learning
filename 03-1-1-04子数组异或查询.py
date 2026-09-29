from typing import List

class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        xors = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            xors[i + 1] = xors[i] ^ arr[i]

        return [xors[l] ^ xors[r + 1] for l, r in queries]

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(Solution().xorQueries(arr, queries))