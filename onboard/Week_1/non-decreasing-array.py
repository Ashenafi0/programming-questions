class Solution(object):
    def checkPossibility(self, nums):
        check = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                check += 1

                if i == 0:
                    nums[i] = nums[i + 1]  # Modify the first element
                elif i > 0 and nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]  # Modify current element
                else:
                    nums[i + 1] = nums[i]  # Modify the next element
        return check <= 1
