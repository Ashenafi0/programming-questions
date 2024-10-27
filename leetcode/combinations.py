class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtracking(first_num,comb):
            if len(comb)==k:
                ans.append(comb.copy())
                return
            for i in range(first_num,n+1):
                comb.append(i)
                backtracking(i+1,comb)
                comb.pop()
        backtracking(1,[])
        return ans


        