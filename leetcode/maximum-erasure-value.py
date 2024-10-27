class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if set(nums)==len(nums):
            return sum(nums)
        value=defaultdict(int)
        l,r=0,0
        ans=0
        total=0
        while r<len(nums):

            value[nums[r]]+=1
            total+=nums[r]
            while len(value)!=r-l+1:
                value[nums[l]]-=1
                if value[nums[l]]==0:
                    del value[nums[l]]
                total-=nums[l]
                l+=1
            ans=max(ans,total)
            r+=1
        return ans
        