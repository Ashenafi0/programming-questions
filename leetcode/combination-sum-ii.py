class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans=[]
        def bc(cur,pos,target):
            if target==0:
                ans.append(cur.copy())
            if target <=0:
                return
            prev=-1
            for i in range(pos,len(candidates)):
                if prev==candidates[i]:
                    continue
                cur.append(candidates[i])
                bc(cur,i+1,target-candidates[i])
                cur.pop()
                prev=candidates[i]
        bc([],0,target)
        return ans
        

        
            
            
        
        

        