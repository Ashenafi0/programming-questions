class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        ans=[]
        def bc(comb,total,i):
            if len(comb)==k and  total==n :
                ans.append(comb.copy())
                return
            if len(nums)<=i or total>n:
                return 
            comb.append(nums[i])
            bc(comb,total+nums[i],i+1)
            comb.pop()
            bc(comb,total,i+1)
        bc([],0,0)
        return ans
                    

        