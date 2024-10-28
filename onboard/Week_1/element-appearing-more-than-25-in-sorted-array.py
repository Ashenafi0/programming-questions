class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        threshold = n // 4

        for i in range(n - threshold):
            if arr[i] == arr[i + threshold]:
                return arr[i]
