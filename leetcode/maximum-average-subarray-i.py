class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_value=float("-inf")
        average_sum=0
        l=0
        for i in range(len(nums)):
            average_sum+=nums[i]
            if i-l+1==k:
                max_value=max(average_sum,max_value)
                average_sum-=nums[l]
                l+=1
        return max_value/k


                
        