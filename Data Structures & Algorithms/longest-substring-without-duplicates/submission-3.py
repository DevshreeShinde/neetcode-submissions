class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # length=1
        # maxlen=1
        # seen = {s[0]:0}
        # i=0
        # j=i+1
        # while j<len(s):
        #     if s[j] in seen:
        #         i=seen[s[j]]+1
        #         j=i+1
        #         seen = {s[i]:i}
        #         maxlen = max(maxlen, length)
        #         length=1
        #         continue
        #     seen[s[j]]=j
        #     j+=1
        #     length+=1
        # return max(maxlen, length)
        maxlen = 0
        start=0
        length=0
        seen={}
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>=start:
                start=seen[s[i]]+1
            seen[s[i]]=i
            maxlen=max(maxlen,(i-start+1))
        return maxlen
