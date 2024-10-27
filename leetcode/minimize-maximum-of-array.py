class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res=total_sum=nums[0]
        for i in range(1,len(nums)):
            total_sum+=nums[i]
            res=max(res,math.ceil(total_sum/(i+1)))
        return res
        