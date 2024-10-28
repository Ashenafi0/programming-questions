class Solution(object):
    def printVertically(self, s):
       s=s.split(" ")
       res=[]
       n=0
       for word in s:
           n=max(n,len(word))
       for i in range(n):
           word=""
           for j in range(len(s)):
               
               if  len(s[j])>i:
                   word+=s[j][i]
               else:
                   word+=" "
           res.append(word.rstrip())
       return res


    
      

            

        