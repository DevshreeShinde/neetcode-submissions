class Solution:
    def binarysearch(self,nums,target,left,right):
        if left > right:
            return -1
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        if nums[left]<=nums[mid]:#left is sorted
            if nums[left] <= target < nums[mid]:
                return self.binarysearch(nums,target,left,mid-1)
            else:
                return self.binarysearch(nums,target,mid+1,right)
        else:
            if nums[mid] < target <= nums[right]:
                return self.binarysearch(nums,target,mid+1,right)
            else:
                return self.binarysearch(nums,target,left,mid-1)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums,target,0,len(nums)-1)
        