
class Solution(object):
    def majorityElement(self, nums):
        count_freq = defaultdict(int)
        threshold = len(nums) // 3
        ans = set()
        
        for num in nums:
            count_freq[num] += 1
            if count_freq[num] > threshold:
                ans.add(num)
        
        return list(ans)
