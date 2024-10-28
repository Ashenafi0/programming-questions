class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
        