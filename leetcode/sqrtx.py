class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        ans=1
        l=0
        r=x-1
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid<=x:
                ans=max(ans,mid)
                l=mid+1
            else:
                r=mid-1
        return ans    