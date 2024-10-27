class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        subset=[]
        def dfs(i):
            if i>=len(nums):
                temp=subset.copy()
                temp.sort()
                ans.add(tuple(temp))
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return [list(sub) for sub in ans]