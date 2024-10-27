class Solution(object):
    def totalFruit(self, fruits):
        dic={}
        l,r,res=0,0,0
        while r< len(fruits):
            dic[fruits[r]]=dic.get(fruits[r],0)+1
            while len(dic)>2:
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:
                    del dic[fruits[l]]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res




        

        
      
        