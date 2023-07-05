class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0
        i=0
        while(i<=len(nums)-1 and i<=max_jump):
            max_jump=max(max_jump,i+nums[i])
            if max_jump>=len(nums)-1:
                return True
            i+=1
        return False
        