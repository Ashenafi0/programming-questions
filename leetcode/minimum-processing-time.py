class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        min_time=float("-inf")
        j=0
        n=processorTime[j]
        for i in range(len(tasks)-1,-1,-1):
            if (i+1)%4==0:
                n=processorTime[j]
                j+=1
            min_time=max(n+tasks[i],min_time)
        return min_time
            
            


        