class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        curr_sum=0
        for i in range(len(nums)):
            if curr_sum==total_sum-(curr_sum+nums[i]):
                return i
            curr_sum+=nums[i]
        return -1

        