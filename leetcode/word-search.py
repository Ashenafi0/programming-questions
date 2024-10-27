class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col,row=len(board[0]),len(board)
        path=set()
        def dfs(c,r,i):
            if i==len(word):
                return True
            if (c<0 or r<0 or c>=col or r>=row or (c,r) in path or word[i]!=board[r][c] ):
                return False
            path.add((c,r))
            res=(dfs(c,r+1,i+1) or dfs(c+1,r,i+1) or dfs(c,r-1,i+1) or dfs(c-1,r,i+1))
            path.remove((c,r))
            return res
        for r in range(row):
            for c in range(col):
                if dfs(c,r,0):
                    return True
        return False

        