class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim=-(2**32 -1)
        tot=0
        for i in range(len(nums)):
            tot=max(tot+nums[i],nums[i])
            maxim=max(maxim,tot)
        return maxim
            

            
            
