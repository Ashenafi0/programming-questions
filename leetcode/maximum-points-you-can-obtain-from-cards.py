class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
   
        k=len(cardPoints)-k
        if k==0:
            return sum(cardPoints)
        total=sum(cardPoints)
        l,r=0,0
        cur=0
        min_sum=float("inf")
        while r<len(cardPoints):
            cur+=cardPoints[r]
            
            if r-l+1==k:
                min_sum=min(cur,min_sum)
                cur-=cardPoints[l]
                l+=1
            
            r+=1
        return total-min_sum 
            



        