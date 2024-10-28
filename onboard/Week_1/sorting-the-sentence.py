class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        s.sort(key=lambda x:x[-1])
        for i in range(len(s)):
            s[i]=s[i][:len(s[i])-1]
        
        return ' '.join(s)
    
        