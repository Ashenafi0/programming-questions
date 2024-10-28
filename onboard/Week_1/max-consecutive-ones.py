class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l=0
        res=0
        i=0
        while i<len(nums):
            if nums[i]==0:
                if i+1<len(nums):
                    i+=1
                    l=i
                else:
                    return res
            else:
                i+=1
            res=max(res,i-l)
        return res


       
        