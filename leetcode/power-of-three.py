class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def rec(num):
            if num==1:
                return True
            if num%3!=0 or num==0:
                return False
            
            return rec(num//3)
        return rec(n)
            
        