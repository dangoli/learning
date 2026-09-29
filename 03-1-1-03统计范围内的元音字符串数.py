# 判断是否元音->01数组
from typing import List
from itertools import accumulate
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        is_valid = lambda word : word[0] in "aeiou" and word[-1] in "aeiou"
        s = list(accumulate(map(is_valid, words),initial=0))
        return [s[r+1] - s[l] for l,r in queries]

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(Solution().vowelStrings(words, queries))