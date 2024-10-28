class Solution(object):
    def largestGoodInteger(self, num):
        left,right=0,0
        res=float("-inf")
        dic={}
        while right<len(num):
            dic[num[right]]=dic.get(num[right],0)+1
            if right-left+1==3:
                if len(dic)==1:
                    res=max(res,int(num[right]))
                dic[num[left]]-=1
                if dic[num[left]]==0:
                    del dic[num[left]]
                left+=1
            right+=1
        if res==float("-inf"):
            return ""
        else:
            return str(res)+str(res)+str(res)

        
        

        
        