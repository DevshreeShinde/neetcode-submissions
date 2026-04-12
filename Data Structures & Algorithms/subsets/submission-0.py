class Solution:
    def sets(self,nums,curr,ans,index):
        ans.append(curr[:])
        for i in range(index,len(nums)):
            curr.append(nums[i])
            self.sets(nums,curr,ans,i+1)
            curr.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        self.sets(nums,curr,ans,0)
        return ans
        