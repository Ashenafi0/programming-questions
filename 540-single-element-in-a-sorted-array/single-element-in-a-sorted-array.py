class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(r-l)//2 +l
            if mid==len(nums)-1 or mid==0:
                return nums[mid]
            
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            leftSize=mid if nums[mid]==nums[mid+1] else mid-1

            if leftSize%2:
                r=mid-1
            else:
                l=mid+1
            


        