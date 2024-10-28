class Solution(object):
    def isPalindrome(self, x):
        st=str(x)
        r=len(st)-1
        l=0
        while l<r:
            if st[l]!=st[r]:
                return False
            l+=1
            r-=1
        return True
        
        
        
        
        