class Solution(object):
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False

        stack = []
        min_i = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            min_i[i] = min(min_i[i - 1], nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > min_i[j]:
                while stack and stack[-1] <= min_i[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
      
        