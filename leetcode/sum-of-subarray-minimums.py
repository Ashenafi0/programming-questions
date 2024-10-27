class Solution(object):
    def sumSubarrayMins(self, arr):
    
        MOD = 10 ** 9 + 7
        stack = []
        result = 0
        
        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result = (result + arr[j] * (i - j) * (j - k)) % MOD
            stack.append(i)
        
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result = (result + arr[j] * (len(arr) - j) * (j - k)) % MOD
        
        return result