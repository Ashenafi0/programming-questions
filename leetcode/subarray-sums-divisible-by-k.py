class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={0:1}

        prefix_sum=0
        count=0
        
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            rem=prefix_sum%k
            if rem in dic:
                count+=dic[rem]
            dic[rem]=dic.get(rem,0)+1
        return count

        