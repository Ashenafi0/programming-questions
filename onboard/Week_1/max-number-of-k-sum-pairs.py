class Solution(object):
    def maxOperations(self, nums, k):
        if len(nums)==1:
            return 0
        nums.sort()
        l,r=0,len(nums)-1
        operation=0
        while l<r:
            if nums[l]+nums[r]<k:
                l+=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                operation+=1
                l+=1
                r-=1
        return operation


       
        