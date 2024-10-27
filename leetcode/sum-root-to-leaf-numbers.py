# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total_sum=0
        self.k=0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if  node and  not node.right and not node.left:
                self.k=self.k*10+node.val
                self.total_sum+=self.k
                self.k=self.k//10
                return
            if not node:
                return
            self.k=self.k*10+node.val
            dfs(node.left)
            dfs(node.right)
            self.k=self.k//10
        dfs(root)
        return self.total_sum

        