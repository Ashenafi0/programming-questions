class Solution(object):
    def moveZeroes(self, nums):
        placeholder=0
        seeker=0
        while seeker<len(nums):
            if nums[seeker]!=0:
                nums[placeholder],nums[seeker]=nums[seeker],nums[placeholder]
                placeholder+=1
            seeker+=1


        

        
            

                