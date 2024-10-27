class Solution(object):
    def numberOfSubarrays(self, nums, k):
       for i in range(len(nums)):
           if nums[i]%2==0:
               nums[i]=0
           else:
                nums[i]=1
       freq={0:1}
       prefix=0
       res=0
       for i in range(len(nums)):
            prefix+=nums[i]
            diff=prefix-k
            res+=freq.get(diff,0)
            freq[prefix]=freq.get(prefix,0) +1
       return res