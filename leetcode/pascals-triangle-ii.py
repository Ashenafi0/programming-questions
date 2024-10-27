class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def custom(n):
            if n==0:
                return [1]
            if n==1:
                return [1,1]
            ret=custom(n-1)
            pascal=[]
            pascal.append(ret[0])
            for i in range(1,len(ret)):
                pascal.append(ret[i]+ret[i-1])
            pascal.append(ret[-1])
            return pascal
        return custom(rowIndex)

        