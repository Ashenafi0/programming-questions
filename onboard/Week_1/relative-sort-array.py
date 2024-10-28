class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        placeholder=0
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    arr1[placeholder],arr1[j]=arr1[j],arr1[placeholder]
                    placeholder+=1
        arr1[placeholder:] = sorted(arr1[placeholder:])

        return arr1
