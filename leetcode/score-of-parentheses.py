class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        output=0
        for char in s:
            if char=="(":
                stack.append(0)
            else:
                if stack:
                    a=stack.pop()
                    if a==0:
                        if stack:
                            stack[-1]+=1
                        else:
                            output+=1
                    else:
                        a=2*a
                        if stack:
                            stack[-1]+=a
                        else:
                            output+=a
        return output
                        


        