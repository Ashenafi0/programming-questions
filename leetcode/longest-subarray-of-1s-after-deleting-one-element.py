class Solution(object):
    def longestSubarray(self, nums):
        l=0
        count_one=0
        max_conse=0
        for r in range(len(nums)):
            if nums[r]==1:
                count_one+=1
            while r-l+1>count_one+1:
                if nums[l]==1:
                    count_one-=1
                l+=1
            max_conse=max(max_conse,count_one)
        return max_conse-1 if max_conse==len(nums) else max_conse
            
        



        