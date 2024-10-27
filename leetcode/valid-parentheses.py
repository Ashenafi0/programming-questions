class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(","]":"[","}":"{"}
        stack=[]
        for i in range(len(s)):
            if s[i] in dic:
                if stack and stack[-1]==dic[s[i]]:
                    stack.pop()
                else:
                    return False
           
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True

                
           
            

        