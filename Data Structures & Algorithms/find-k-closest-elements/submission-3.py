class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        seen = [(num, abs(num - x)) for num in nums]
        seen.sort(key=lambda x: (x[1], x[0]))
        ans = []
        
        for key,val in seen:
            ans.append(key)
            if len(ans)==k:
                break
        return sorted(ans)