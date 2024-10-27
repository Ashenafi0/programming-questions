# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_val=float("-inf")
        self.stack=[]
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                self.max_val=max(self.max_val,abs(max(self.stack)-min(self.stack)))
                return
            self.stack.append(node.val)
            dfs(node.left)
            dfs(node.right)
            self.stack.pop()
        dfs(root)
            
            
        
        return self.max_val
        