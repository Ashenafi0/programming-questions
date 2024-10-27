class Solution:
    def maxScore(self, s: str) -> int:
        
        no_one=s.count("1")
        no_zero=s.count("0")

        count_one=0
        count_zero=0
        score=0
        for i in range(len(s)-1):
            if s[i]=="0":
                count_zero+=1
            else:
                count_one+=1
            score=max(score,count_zero+no_one-count_one)
        return score
            



        