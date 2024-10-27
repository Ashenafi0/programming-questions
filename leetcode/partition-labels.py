class Solution(object):
    def partitionLabels(self, s):
        lastindex={}
        for i,num in enumerate(s):
            lastindex[num]=i
        res=[]
        end,size=0,0
        for j in range(len(s)):
            size+=1
            end=max(end,lastindex[s[j]])
            if end==j:
                res.append(size)
                size=0
        return res


        
        