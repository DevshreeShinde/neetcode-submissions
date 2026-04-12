class Solution:
    def combination(self,nums,target,curr,ans,index):
        if target==0:
            ans.append(curr[:])
            return
        for i in range(index,len(nums)):
            if nums[i]>target:
                continue
            curr.append(nums[i])
            self.combination(nums,target-nums[i],curr,ans,i)
            curr.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr=[]
        self.combination(nums,target,curr,ans,0)
        return ans