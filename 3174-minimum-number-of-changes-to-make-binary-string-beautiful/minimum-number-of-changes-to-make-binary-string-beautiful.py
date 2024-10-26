class Solution:
    def minChanges(self, s: str) -> int:
        
        cv=s[0]
        changes=0
        size=0

        for ch in s:
            
            if ch !=cv:
                if size%2!=0:
                    changes+=1
                    size+=1
                else:
                    cv=ch
                    size=1
            else:
                size+=1
        return changes


                    



        
            
        