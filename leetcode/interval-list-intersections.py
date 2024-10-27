class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        p1,p2=0,0
        ans=[]
        while p1<len(firstList) and p2<len(secondList):
            
            start1=firstList[p1][0]
            end1=firstList[p1][1]
            start2=secondList[p2][0]
            end2=secondList[p2][1]
            if start2<=end1 and end2>=start1:
                ans.append([max(start1,start2),min(end1,end2)])
            if end1>end2:
                p2+=1
            else:
                p1+=1
      
        return ans


        