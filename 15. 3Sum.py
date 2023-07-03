class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        arr=sorted(nums)
        for i in range(len(arr)-2):
            j=i+1
            k=len(arr)-1
            while(j<k):
                #print(arr[i]+arr[j]+arr[k])
                if arr[i]+arr[j]+arr[k]==0:
                    ans.add((arr[i],arr[j],arr[k]))
                    j+=1
                    k-=1
                elif arr[i]+arr[j]+arr[k]<0:
                    j+=1
                else:
                    k-=1
        return ans