class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {} 

        for i ,num in enumerate(nums):
            difference=target-num
            if num in num_to_index:
                return [num_to_index[num],i]
            if difference not in num_to_index:
                num_to_index[difference]=i
       