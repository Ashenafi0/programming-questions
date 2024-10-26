class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l=0
        rem=0
        for i in range(1,len(colors)):
            if colors[l]==colors[i]:
                if neededTime[l]>neededTime[i]:
                    rem+=neededTime[i]
                else:
                    rem+=neededTime[l]
                    l=i

            else:
                l=i
        return rem