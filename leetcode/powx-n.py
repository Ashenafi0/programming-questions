class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,y):
            if y==0:
                return 1
            res=pow(x,y//2)
            res*=res
            if y%2!=0:
                res*=x
            return res
        result=pow(x,abs(n))
        if n<0:
            return 1/result
        return result
        