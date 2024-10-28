class Solution(object):
    def sumOfThree(self, num):
        if num%3==0:
            x=num/3
            return [x-1,x,x+1]   
        else:
            return []
        
        