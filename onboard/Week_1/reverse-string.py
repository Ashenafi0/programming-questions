class Solution(object):
    def reverseString(self, s):
        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
            

        
        