class NumArray(object):

    def __init__(self, nums):
      
        self.prefixSum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prefixSum[i+1]=self.prefixSum[i]+nums[i]
        

    def sumRange(self, left, right):
      return self.prefixSum[right+1]-self.prefixSum[left]
        
          
       
           
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)