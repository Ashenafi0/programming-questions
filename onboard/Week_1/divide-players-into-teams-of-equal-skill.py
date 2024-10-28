class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        left,right=0,len(skill)-1
        res=0
        lastsum=skill[0]+skill[-1]
        while left<right:
            if skill[left]+skill[right]!=lastsum:
                return -1
            else:
                res+=skill[left]*skill[right]
            left+=1
            right-=1
        return res
        



       
            
        

      
        