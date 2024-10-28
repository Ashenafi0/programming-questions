class Solution(object):
    def checkPowersOfThree(self, n):
        def rec(n):
            if n==1 or n==0:
                return True
            if n%3==1 or n%3==0:
                
                return rec(n/3)
            else:
                return False
        return rec(n)
                
        

        
        