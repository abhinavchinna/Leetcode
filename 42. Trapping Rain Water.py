class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=[height[0]]
        for i in range(1,n):
            l.append(max(l[i-1],height[i]))
        r=[height[n-1] for i in range(n)]
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],height[i])
        #print(l,r,sep="\n")
        c=0
        for i in range(n):
            c+=(min(l[i],r[i])-height[i])
        return c

