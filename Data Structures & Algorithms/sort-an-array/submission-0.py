class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(start,end):
            if start>=end:
                return
            middle=(start+end)//2
            mergesort(start,middle)
            mergesort(middle+1,end)
            merge(start,middle, end)
        
        def merge(start,middle,end):
            i =start
            j=middle+1
            tmp=[]
            while i<=middle and j<=end:
                if nums[i]<=nums[j]:
                    tmp.append(nums[i])
                    i+=1
                else:
                    tmp.append(nums[j])
                    j+=1
            while i<=middle:
                tmp.append(nums[i])
                i+=1
            while j<=end:
                tmp.append(nums[j])
                j+=1
            for i in range(len(tmp)):
                nums[start+i]=tmp[i]
        mergesort(0,len(nums)-1)
        return nums