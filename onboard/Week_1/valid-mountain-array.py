class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        max_val=max(arr)
        if arr.index(max_val)==0 or arr.index(max_val)==len(arr)-1:
            return False
        for i in range(arr.index(max_val)):
            if arr[i]>=arr[i+1]:
                return False
        for i in range(arr.index(max_val),len(arr)-1):
            if arr[i]<=arr[i+1]:
                return False
        return True
            