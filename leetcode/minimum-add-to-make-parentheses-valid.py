class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]

        for char in s:
            print(char)
            if char=="(":
                stack.append(char)
            else:
                if stack:
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
        return len(stack)
        
        