class Solution(object):
    def romanToInt(self, s):
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        if len(s)==1:
            res=dic[s[0]]
            return res
        i=0

        while i < len(s)-1:
            if dic[s[i]]<dic[s[i+1]]:
                res+=dic[s[i+1]]-dic[s[i]]
                i+=2
                if i==len(s)-1:
                    res+=dic[s[i]]
            else:
                res+=dic[s[i]]
                i+=1
                if i==len(s)-1:
                    res+=dic[s[i]]
        return res


        
        