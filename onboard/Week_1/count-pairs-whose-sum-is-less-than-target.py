class Solution(object):
    def countPairs(self, nums, target):
        if len(nums)==0:
            return 0
        nums.sort()
        l,r=0,len(nums)-1
        count=0
        while l<r:
            total=nums[l]+nums[r]
            if total <target:
                count+=r-l
                l+=1
            else:
                r-=1
        return count


       
        