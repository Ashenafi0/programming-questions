class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que=deque(tickets)
        time=0

        while que[k]>0:
            if que[k]==1:
                for i in range(k+1):
                    a=que.popleft()
                    if a:
                        time+=1
                        a-=1
                    que.append(a)
                return time

            for i in range(len(que)):
                a=que.popleft()
                if a:
                    time+=1
                    a-=1
                que.append(a)
            
        return time
                
        
        

        
        