class Solution(object):
    def longestOnes(self, nums, k):
        dic={0:0,1:0}
        res=float("-inf")
        l=0
        for r in range(len(nums)):
            dic[nums[r]]+=1
            while dic[0]>k:
                dic[nums[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res

       
            


       
        