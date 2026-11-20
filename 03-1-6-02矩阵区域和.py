from typing import List

class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        s = [[0] * (n+1) for _ in range(m+1)]

        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] -s[i][j] + mat[i][j]

        # 确保下标不会溢出
        def get(x,y):
            a = max(min(m, x),0)
            b = max(min(n, y),0)
            return s[a][b]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i+k+1, j+k+1) - get(i+k+1, j-k) - get(i-k,j+k+1) + get(i-k,j-k)

        return ans

mat = [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]]
k = 3
s = Solution()
print(s.matrixBlockSum(mat, k))