class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def dfs(string):
            if len(string)<2:
                return ""
            hashset=set(string)
            for i in range(len(string)):
                if not (string[i].lower() in hashset and string[i].upper() in hashset):
                    string1=dfs(string[:i])
                    string2=dfs(string[i+1:])
                    return string1 if len(string1)>=len(string2) else string2
            return string
        return dfs(s)
    
            
            