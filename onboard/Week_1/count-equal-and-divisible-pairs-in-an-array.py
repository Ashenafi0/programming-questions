class Solution(object):
    def countPairs(self, nums, k):
        dic={}
        count=0
        for i in range(len(nums)):
            if nums[i] in dic:
                for j in range(len(dic[nums[i]])):
                    if (dic[nums[i]][j]*i)%k==0:
                        count+=1
            
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]]=[i]
        return count
        
        