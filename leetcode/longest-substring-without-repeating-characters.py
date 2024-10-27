class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        max_len=0
        l=0
        for i in range(len(s)):
            if s[i] in dic:
                while s[i] in dic:
                    dic[s[l]]-=1
                    
                    if dic[s[l]]==0:
                        del dic[s[l]]
                    l+=1
                
            dic[s[i]]=1
            max_len=max(i-l+1,max_len)
        return max_len
            


        