from typing import List

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix) # 矩阵的行数
        n = len(matrix[0]) # 矩阵的列数
        s = [[0] * (n+1) for _ in range(m+1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + x
        self.s = s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.s
        return s[row2+1][col2+1] - s[row2+1][col1] - s[row1][col2+1] + s[row1][col1]

ops = ["NumMatrix","sumRegion","sumRegion","sumRegion"]
args = [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
obj = None
res = []

for op, arg in zip(ops, args):
    if op == "NumMatrix":
        obj = NumMatrix(*arg)
        res.append(None)
    else:
        res.append(obj.sumRegion(*arg))

print(res)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)