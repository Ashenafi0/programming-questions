class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        print(path)
        stack=[]

        for char in path:
            if char=="..":
                if stack:
                    stack.pop()
            elif char=="/" or char=="." or char == '':
                continue
            else:
                stack.append(char)
        return "/"+ "/".join(stack)
        