class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        def count(k):
            c=0
            for i in range(0,32):
                if k&(1<<i):
                    c+=1
            return c
        for j in range(n+1):
            ans.append(count(j))
        return ans