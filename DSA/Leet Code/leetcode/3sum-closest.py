

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("inf")

        for i in range(len(nums)):
            a = nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                total_sum = a + nums[l] + nums[r]

                if abs(target - total_sum) < abs(target - closest_sum):
                    closest_sum = total_sum

                if total_sum < target:
                    l += 1
                else:
                    r -= 1

        return closest_sum
