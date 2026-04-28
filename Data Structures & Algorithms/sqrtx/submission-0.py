class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left<=right:
            middle = (left+right)//2
            currsq = middle*middle
            if currsq==x:
                return middle
            elif currsq<x:
                left=middle+1
            else:
                right=middle-1
        return right