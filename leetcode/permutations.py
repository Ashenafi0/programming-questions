class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        que=deque(nums)
        ans=[]
        def backtrac(values):
            if len(values)==len(nums):
                ans.append(values.copy())
                return
            for i in range(len(que)):
                temp=que.popleft()
                values.append(temp)
                backtrac(values)
                values.pop()
                que.append(temp)
            


        backtrac([])
        return ans
    
                
    

        