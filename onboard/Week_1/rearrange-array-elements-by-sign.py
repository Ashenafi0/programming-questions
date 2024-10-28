class Solution(object):
    def rearrangeArray(self, nums):
        posetive_num=[]
        negetive_num=[]
        for i in range(len(nums)):
            if nums[i]>0:
                posetive_num.append(nums[i])
            else:
                negetive_num.append(nums[i])
        ans=[]
        for i in range(len(negetive_num)):
            ans.append(posetive_num[i])
            ans.append(negetive_num[i])
        return ans



        
        