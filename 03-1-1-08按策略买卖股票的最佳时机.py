from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        c = [0] * len(prices)
        for i in range(len(prices)):
            c[i] = prices[i] * strategy[i]
        sum = [0] * (len(prices) + 1)
        sumShell = [0] * (len(prices)+1)
        for i in range(len(prices)):
            sum[i+1] = sum[i] + c[i]
            sumShell[i+1] = sumShell[i] + prices[i]

        #不改的话，返回sum[-1]
        #改的话，分ABCD四个区域计算新的c值
        #A改前sum
        #B0
        #Csumshell
        #Dsum,

        pre = max(sum[i-k] + sumShell[i] - sumShell[i - k//2] + sum[len(prices)] - sum[i] for i in range(k, len(prices)+1))
            
        return max(pre, sum[-1])

prices = [5,8]
strategy = [-1,-1]
k = 2

s = Solution()
print(s.maxProfit(prices, strategy, k))