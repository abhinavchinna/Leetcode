class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=0
        num=x
        while(num>0):
            s*=10
            s+=num%10
            num//=10
        if s==x:
            return True
        else:
            return False