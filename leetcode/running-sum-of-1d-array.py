class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        runningSum=[]
        
        for i in range(len(nums)):
            sum+=nums[i]
            nums[i]=sum
        return nums
            

            