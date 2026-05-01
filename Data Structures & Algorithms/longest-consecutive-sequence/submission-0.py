class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length =0
        longest = 0
        nums_set=set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                length=1
                curr=num
                while curr+1 in nums_set:
                    curr+=1
                    length+=1
                longest=max(length,longest)
        return longest