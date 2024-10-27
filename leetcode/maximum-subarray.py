class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        prefix_sum=0
        largest_sum=float("-inf")

        for i in range(len(nums)):
            
            if prefix_sum<0:
                largest_sum=max(largest_sum,nums[i])
                prefix_sum=nums[i]
            else:
                prefix_sum+=nums[i]
                largest_sum=max(largest_sum,prefix_sum)
        return largest_sum


        