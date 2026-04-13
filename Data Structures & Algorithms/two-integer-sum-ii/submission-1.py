class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        n=len(numbers)-1

        while(i<n):
            if numbers[i]+numbers[n]==target:
                return [i+1,n+1]
            elif numbers[i]+numbers[n]>target:
                n-=1
            else:
                i+=1

        return []