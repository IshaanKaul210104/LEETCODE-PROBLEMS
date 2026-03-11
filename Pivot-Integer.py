class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            leftSum = i*(i + 1) // 2
            rightSum = (n*(n + 1) // 2) + i - leftSum
            if leftSum == rightSum:
                return i
        return -1
