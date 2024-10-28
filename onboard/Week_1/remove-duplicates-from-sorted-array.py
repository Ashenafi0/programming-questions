class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        placeholder=1
        seeker=1
        count=1
        while seeker<len(nums):
            if nums[seeker]!=nums[seeker-1]:
                nums[placeholder]=nums[seeker]
                placeholder+=1
            seeker+=1
        return placeholder

        