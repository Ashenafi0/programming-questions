class Solution(object):
    def pivotArray(self, nums, pivot):
        ans=[0]*len(nums)
        placeholder=0
        i=0
        while i<len(nums):
            if nums[i]<pivot:
                ans[placeholder]=nums[i]
                placeholder+=1
            i+=1
        i=placeholder
        j=len(nums)-1
        placeholder=len(nums)-1
        while j>=0:
            if nums[j]>pivot:
                ans[placeholder]=nums[j]
                placeholder-=1
            elif nums[j]==pivot:
                ans[i]=nums[j]
                i+=1

            j-=1
        return ans


        



        
        