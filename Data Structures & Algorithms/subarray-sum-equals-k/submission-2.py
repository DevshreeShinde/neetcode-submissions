class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #nums_set = set(nums)
        hash_set = {0:1}
        count = 0
        curr_sum=0
        for num in nums:
            curr_sum += num
            if curr_sum-k in hash_set:
                count+=hash_set[curr_sum-k]
            hash_set[curr_sum]=hash_set.get(curr_sum,0)+1
        return count
        