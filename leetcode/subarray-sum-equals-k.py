class Solution(object):
    def subarraySum(self, nums, k):
        dic={0:1}
        res=0
        cursum=0
        for i in range(len(nums)):
            cursum+=nums[i]
            diff=cursum-k
            res+=dic.get(diff,0)
            dic[cursum]=dic.get(cursum,0)+1
        return res

        
        