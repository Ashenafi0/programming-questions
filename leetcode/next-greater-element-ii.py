class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[-1]*len(nums)
        stack2=[]
        for i in range(2*len(nums)):
            while stack2 and stack2[-1][0]<nums[i%len(nums)]:
                num,j=stack2[-1]
                stack[j]=nums[i%len(nums)]
                stack2.pop()
            stack2.append([nums[i%len(nums)],i%len(nums)])
        return stack
                
