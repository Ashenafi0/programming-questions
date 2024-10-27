class Solution(object):
    def pancakeSort(self, arr):
        result=[]
        def flip(k):
            arr[:k]=arr[:k][::-1]
            result.append(k)
        def find_max(end):
            max_value=float("-inf")
            index_val=0
            for x in range(end):
                if arr[x]>max_value:
                    max_value=arr[x]
                    max_index=x
            return max_index
        n=len(arr)
        while n>1:
            max_index=find_max(n)
            if max_index!=n-1:
                if max_index!=0:
                    flip(max_index + 1)
                flip(n)
            n-=1
        return result
        

