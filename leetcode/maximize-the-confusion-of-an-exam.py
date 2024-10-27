class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        r=0
        dic={"T":0,"F":0}
        ans=0
        while r<len(answerKey):
            dic[answerKey[r]]+=1
            while l<r and min(dic["T"],dic["F"])>k:
                dic[answerKey[l]]-=1
                l+=1
                
            
            ans=max(ans,r-l+1)
            r+=1
        return ans

        
            



        