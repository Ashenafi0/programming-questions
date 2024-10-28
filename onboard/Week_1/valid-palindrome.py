class Solution(object):
    def isPalindrome(self, s):
        s="".join(s)
        ans=[char.lower() for char in s if char.isalnum()]
        ans=list(ans)
        i,j=0,len(ans)-1
        
        while i<j:
            if ans[i]!=ans[j]:
                return False
            i+=1
            j-=1
        return True
        