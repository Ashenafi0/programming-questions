class Solution(object):
    def average(self, salary):
       salary.sort()
       totalsum=sum(salary[1:len(salary)-1])/1.00000
       n=len(salary[1:len(salary)-1])
       return totalsum/n
        
        