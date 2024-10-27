class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum=0
        total_sum=sum(nums)
        output=[]

        for i in range(len(nums)):
            output.append(i*nums[i]-prefix_sum+(total_sum-nums[i]-(len(nums)-(i+1))*nums[i]))
            prefix_sum+=nums[i]
            total_sum-=nums[i]
        return output
        