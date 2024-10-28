class Solution(object):
    def threeSum(self, nums):
       res=[]
       nums.sort()
       for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
               continue
            l,r=i+1,len(nums)-1
            while l<r:
                threeSum=nums[i]+nums[l]+nums[r]
                if threeSum >0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
       return res

        

      
        