class Solution(object):
    def minimumRecolors(self, blocks, k):
        l=0
        track=0
        res=float("inf")
        for r in range(len(blocks)):
            if blocks[r]=="W":
                track+=1
            if (r-l +1)==k:
                res=min(res,track)
                if blocks[l]=="W":
                    track-=1
                l+=1
           
            
        return res

        
        