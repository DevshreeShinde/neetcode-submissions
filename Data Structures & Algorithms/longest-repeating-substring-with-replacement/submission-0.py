class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        res = 0
        maxval = 0
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0)+1
            maxval = max(maxval,seen[s[right]])

            while right - left + 1 - maxval > k:
                seen[s[left]]-=1
                left+=1
            res = max(res, right - left + 1)
        return res
        
        