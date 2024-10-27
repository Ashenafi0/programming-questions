class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        prefix_sum=[0]*len(nums)
        mode=10**9 +7

        for i in range(len(requests)):
            start,end=requests[i]
            prefix_sum[start]+=1
            if end+1<len(nums):
                prefix_sum[end+1]-=1
        accumulator=0
        for i in range(len(prefix_sum)):
            accumulator+=prefix_sum[i]
            prefix_sum[i]=accumulator
        prefix_sum.sort()
        nums.sort()
        result=0
        for i in range(len(nums)):
            result+=(prefix_sum[i]*nums[i])
        
        return result%mode


            

        