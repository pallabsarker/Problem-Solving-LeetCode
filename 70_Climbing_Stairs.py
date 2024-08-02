class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev1 = 0, 1
        while n > 0:
            output = prev2 + prev1
            prev2 = prev1
            prev1 = output
            n -= 1
        return output
