class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        start=0
        sum=nums[0]
        for i in range(1,len(nums)):
            if sum<0:
                start=i
                sum=0
            sum=sum+nums[i]
            max_sum=max(max_sum,sum)
        return max_sum


        