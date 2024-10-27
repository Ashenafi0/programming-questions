class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        ans=r

        def check(cap):
            curr_cap=cap
            day=1
            for w in weights:
                if curr_cap-w<0:
                    day+=1
                    curr_cap=cap
                curr_cap-=w
            return day<=days


        while l<=r:
            cap=l+(r-l)//2
            if check(cap):
                ans=min(ans,cap)
                r=cap-1
            else:
                l=cap+1
        return ans
        
        
        