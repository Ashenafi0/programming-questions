class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        dic={0:1}

        curr_sum=0
        count=0

        for i in range(len(nums)):
            curr_sum+=nums[i]
            diff=curr_sum-goal
            if diff in dic:
                count+=dic[diff]
            dic[curr_sum]=dic.get(curr_sum,0)+1
        return count
