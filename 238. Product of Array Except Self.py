class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1 for i in range(n)]
        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        right=[1 for i in range(n)]
        right[n-1]=1
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        ans=[]
        for i in range(n):
            ans.append(left[i]*right[i])
        return(ans)
                