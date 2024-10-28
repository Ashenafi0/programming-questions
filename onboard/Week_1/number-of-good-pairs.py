class Solution(object):
    def numIdenticalPairs(self, nums):
        dic = {}
        res = 0
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for num in dic:
            n = dic[num]
            if n != 1:
                res += (n * (n - 1)) // 2
        return res
