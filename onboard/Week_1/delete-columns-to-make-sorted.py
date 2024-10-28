class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m=len(strs)
        n=len(strs[0])
        deleted=0
        for i in range(n):
            for j in range(1,m):
                if ord(strs[j-1][i])>ord(strs[j][i]):
                    deleted+=1
                    break
        return deleted

        