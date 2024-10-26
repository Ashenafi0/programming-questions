class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr=0
        left,right=1,2**(n-1)

        for _ in range(n-1):
            mid=(right+left)//2

            if k<=mid:
                right=mid
            else:
                left=mid+1
                curr=0 if curr else 1
        return curr
        