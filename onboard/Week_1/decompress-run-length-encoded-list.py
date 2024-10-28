class Solution(object):
    def decompressRLElist(self, nums):
        n=len(nums)//2
        res=[]
        for i in range(n):
            freq,val=nums[2*i],nums[2*i+1]
            for _ in range(freq):
                res.append(val)
        return res



       
        