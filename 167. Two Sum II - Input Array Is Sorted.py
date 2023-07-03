class Solution:
    def binarysearch(self,arr,key,start):
        l=start
        h=len(arr)-1
        while(l<=h):
            mid=(l+h)//2
            if key==arr[mid]:
                return mid
            elif key<arr[mid]:
                h=mid-1
            else:
                l=mid+1
        return False
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            next_index=self.binarysearch(numbers,target-numbers[i],i+1)
            if next_index:
                return [i+1,next_index+1]