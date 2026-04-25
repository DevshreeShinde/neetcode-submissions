class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left<right:
            mid = (left+right)//2
            ans = 0
            for pile in piles:
                ans += (pile + mid - 1) // mid
            if ans<=h:
                right=mid
            else:
                left=mid+1
        return left
        