class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
  
        def dfs(values,i,total):
            if i<len(candidates) and total==target:
                ans.append(values.copy())
                return
            if total>target or i>=len(candidates):
                return
            values.append(candidates[i])
            total+=candidates[i]
            dfs(values,i,total)
            values.pop()
            total-=candidates[i]
            
            dfs(values,i+1,total)
        dfs([],0,0)
        return ans
            
        