class Solution(object):
    def characterReplacement(self, s, k):
        dic={}
        l=0
        res=0
        for r in range(len(s)):
            dic[s[r]]=dic.get(s[r],0)+1
            while (r-l +1 )-max(dic.values())>k:
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
            res=max(res,r-l+1)
        return res

        
    



      

        
        
            
        