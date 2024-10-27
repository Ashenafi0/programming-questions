class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        distinct = len(set(nums))
        freq = {}
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            while len(freq) == distinct:
                ans += len(nums) - r
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
        return ans
