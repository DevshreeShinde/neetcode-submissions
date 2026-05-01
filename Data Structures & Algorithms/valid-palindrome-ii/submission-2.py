class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return ispalindrome(left,right-1)or ispalindrome(left+1,right)
            left+=1
            right-=1
        return True 
        