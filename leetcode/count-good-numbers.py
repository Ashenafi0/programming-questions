class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=(7+10**9)

        def pow(x,y):
            if y==0:
                return 1
            res=pow(x,y//2)
            res=(res*res)%mod
            if y%2!=0:
                res=(res*x)%mod
            return res
        
        count=pow(5,(n+1)//2)
        count*=pow(4,(n)//2)

        
        
            
        return count%(7+10**9)

        