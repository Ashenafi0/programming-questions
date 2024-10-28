class Solution(object):
    def applyOperations(self, nums, operations):
      
        num_to_index = {num: i for i, num in enumerate(nums)}
        
        for old_num, new_num in operations:
            index = num_to_index[old_num]
            nums[index] = new_num
            del num_to_index[old_num]
            num_to_index[new_num] = index
        
        return nums
    
    def arrayChange(self, nums, operations):
      
        nums = self.applyOperations(nums, operations)
        
        return nums