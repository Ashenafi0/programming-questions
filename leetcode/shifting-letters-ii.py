from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        ps=[0]*len(s)

        for start,end,value in shifts:
            if value==1:
                ps[start]+=1
                if end+1<len(ps):
                    ps[end+1]-=1
            else:
                ps[start]-=1
                if end+1<len(ps):
                    ps[end+1]+=1
        accumulator=0
        prefix_sum=[]
        for i in range(len(ps)):
            accumulator+=ps[i]
            prefix_sum.append(accumulator)
        
        output=""
        print(prefix_sum)
        for i in range(len(s)):
           
            temp = (ord(s[i]) + prefix_sum[i]-ord("a"))%26 + ord("a")
            output += chr(temp)
            
        return output
