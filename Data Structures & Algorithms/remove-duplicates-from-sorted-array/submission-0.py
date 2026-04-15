class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        k=1
        i=1
        while i<len(nums):
            if nums[i-1]!=nums[i]:
                nums[k]=nums[i]
                k+=1
            i+=1
        return k
        