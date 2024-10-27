class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        output=0
        for i in range(2,len(nums)):
            l,r=0,i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    output+=r-l
                    r-=1
                else:
                    l+=1
        return output
            
        


        