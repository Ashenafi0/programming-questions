class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_value=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            ans.append(sorted_value.index(nums[i]))
        return ans

        