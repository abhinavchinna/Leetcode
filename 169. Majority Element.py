class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=nums[0]
        n=len(nums)
        c=1
        for i in range(1,n):
            if nums[i]==majority:
                c+=1
            elif c==0 and majority!=nums[i]:
                majority=nums[i]
                c+=1
            else:
                c-=1
        return majority
            