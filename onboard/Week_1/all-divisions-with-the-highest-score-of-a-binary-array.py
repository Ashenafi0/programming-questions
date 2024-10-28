class Solution(object):
    def maxScoreIndices(self, nums):
        count_one=nums.count(1)
        count_zero=0
        i=0
        max_score=0
        dic={}
        while i<len(nums):
            score =count_zero + count_one
            if i==0:
                dic[score]=[i]
            else:
                if score in dic:
                    dic[score].append(i)
                else:
                    dic[score]=[i]
            max_score=max(max_score,score)
            if nums[i]==1:
                count_one-=1
            if nums[i]==0:
                count_zero+=1
            i+=1
        if count_zero in dic:
            dic[count_zero].append(len(nums))
        else:
            dic[count_zero]=[len(nums)]
            max_score=max(max_score,count_zero)
        return dic[max_score]
            


        
        