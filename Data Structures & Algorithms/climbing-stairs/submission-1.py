class Solution:
    def climb(self,steps,n):
        if n<=1:
            return 1
        if steps[n]!=-1:
            return steps[n]
        steps[n]=self.climb(steps,n-1)+self.climb(steps,n-2)
        return steps[n]
    def climbStairs(self, n: int) -> int:
        steps = [-1] * (n + 1)
        return self.climb(steps,n)
        