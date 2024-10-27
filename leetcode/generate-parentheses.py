class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        stack=[]
        def bc(openN,closeN):
            if openN==closeN==n:
                ans.append("".join(stack))
            if openN<n:
                stack.append("(")
                bc(openN+1,closeN)
                stack.pop()
            if openN>closeN:
                stack.append(")")
                bc(openN,closeN+1)
                stack.pop()
        bc(0,0)
        return ans





        