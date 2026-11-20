class NumArray:

    def __init__(self, nums: list[int]):
        s = [0] * (len(nums) + 1)
        
        for i in range(0, len(nums) ):
            s[i+1] = s[i] + nums[i]

        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]

ops = ["NumArray", "sumRange", "sumRange", "sumRange"]
args = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

obj = None
res = []

for op, arg in zip(ops, args):
    if op == "NumArray":
        obj = NumArray(*arg)
        res.append(None)
    else:
        res.append(obj.sumRange(*arg))

print(res)