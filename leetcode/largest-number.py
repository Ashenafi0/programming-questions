class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def helper(element1,element2):
            return str(element1)+str(element2)<str(element2)+str(element1)
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if helper(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        last_ans="".join(map(str, nums))
        last_ans=int(last_ans)
        return str(last_ans)

        