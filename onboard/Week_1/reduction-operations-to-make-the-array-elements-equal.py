class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if nums.count(nums[0])==len(nums):
            return 0
        nums.sort(reverse=True)
        
        dic=defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]]+=1
        
        keys_list = list(dic.keys())
        ans=0
        prefix=0
        for i in range(len(keys_list)-1):
            prefix+=dic[keys_list[i]]
            ans+=prefix
        return ans


        
        