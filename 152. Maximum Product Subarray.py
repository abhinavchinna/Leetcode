class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_=curr_min=curr_max=nums[0]
        for i in range(1,len(nums)):
            prev_curr_max=curr_max
            curr_max=max(nums[i],max(curr_min*nums[i],curr_max*nums[i]))
            curr_min=min(nums[i],min(curr_min*nums[i],prev_curr_max*nums[i]))
            max_=max(curr_max,max_)
        return max_


            
