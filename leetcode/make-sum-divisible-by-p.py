class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dic={0:0}

        prefix_sum=0
        output=float("inf")
        
        rem=sum(nums)%p
        if rem==0:
            return 0
        elif rem==sum(nums):
            return -1
            
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            diff=(prefix_sum%p-rem)%p
            if diff in dic:
                output=min(output,i-dic[diff]+1)
            dic[prefix_sum%p]=i+1
        
        return -1 if output>=len(nums) else output

        