class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if  not stack or stack[-1][0]>temperatures[i]:
                stack.append([temperatures[i],i])
            else:
                while stack and stack[-1][0]<temperatures[i]:
                    num,j=stack[-1]
                    output[j]=i-j
                    stack.pop()
                stack.append([temperatures[i],i])
        return output

        