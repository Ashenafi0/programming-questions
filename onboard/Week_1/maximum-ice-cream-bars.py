class Solution(object):
    def maxIceCream(self, costs, coins):
        count=[0]*(max(costs)+1)
        sorted_costs=[]
        for i in range(len(costs)):
            count[costs[i]]+=1
        for i in range(len(count)):
            while count[i]!=0:
                sorted_costs.append(i)
                count[i]-=1
        no_icecream=0
        cost=0
        for i in range(len(sorted_costs)):
            cost+=sorted_costs[i]
            if cost>coins:
                return no_icecream
            no_icecream+=1
        return no_icecream
            

        
        