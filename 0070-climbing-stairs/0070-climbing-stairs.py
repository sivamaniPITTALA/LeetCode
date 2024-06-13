class Solution:
    def climbStairs(self, n: int) -> int:
        a = 2
        b = 3
        if n <= 3:
            return n
        for i in range(n-3):
            temp = a
            a = b
            b += temp
        return b
