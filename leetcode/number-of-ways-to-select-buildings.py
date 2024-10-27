class Solution:
    def numberOfWays(self, s: str) -> int:
        count_1=s.count("1")
        count_0=s.count("0")
        cur_1=0
        cur_0=0
        ans=0
        for i in range(len(s)):
            if s[i]=="0":
                ans+=(cur_1*(count_1-cur_1))
                cur_0+=1
            if s[i]=="1":
                ans+=(cur_0*(count_0-cur_0))
                cur_1+=1
            
        return  ans
                
                



        
        
        
        