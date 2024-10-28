class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right=0,len(nums)-1
        seeker=0
        while seeker<=right:
            if nums[seeker]==0:
                nums[seeker],nums[left]=nums[left],nums[seeker]
                left+=1
            elif nums[seeker]==2:
                nums[seeker],nums[right]=nums[right],nums[seeker]
                right-=1
                seeker-=1
            seeker+=1
        return nums

        