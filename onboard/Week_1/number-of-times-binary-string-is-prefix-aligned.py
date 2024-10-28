class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count_one=0
        count_index=0
        ans=0
        for i in range(len(flips)):
            count_index +=(i+1)
            count_one +=flips[i]
            if count_index==count_one:
                ans+=1
        return ans


        